---
exclude_from_lunr: true
---
'use strict'
// Create a new map inside the DIV element with the id 'home_page_map' and create
// a centroid marker that represents the bound of the data. Generate markers for each
// record, where each marker represent the location of that record
function initHomePageMap() {
  // The centre point
  var centreLatLng = {lat: 42.6169, lng: 25.2848};
  // HTML element for which the map will be generated under.
  var homePageMapHTMLElement = document.getElementById('home_page_map');
  // Create a new map inside the homePageMapHTMLElement.
  var map = new google.maps.Map(homePageMapHTMLElement, {
   center: centreLatLng,
   zoom: 11
  });
  {% comment %}
    For each record, store the title, latitude and longitude of that record into
    a dict and store that into a list. Capture that list as a string and store
    it into the variable called 'markers'.
  {% endcomment %}

  {% capture markers %}
  [
  {% for post in site.posts %}
  {"title":"{{ post.title }}","lat":"{{ post.latitude}}","lng":"{{ post.longitude }}"}
  {%- if forloop.last -%}{%- else -%},{%- endif -%}
  {% endfor %}
  ]
  {% endcapture %}

  // Assign the value of markers into the Javascript variable markers. Remove any
  // newline characters from the string before assignment.
  var markers = {{ markers | strip_newlines }};

  // For each record, generate the marker.
  for(var i = 0; i < markers.length; i++){
    var latLng = new google.maps.LatLng(markers[i].lat, markers[i].lng);
    var marker = new google.maps.Marker({
      position: latLng,
      title: markers[i].title
    });
    marker.setMap(map);
  }

  var RED = '#FF0000'; // Deep RED Color in HEX
  var RADIUS_AREA = 15 * 1000; // In metres so 15km

  // Generate the centroid that covers the bounds of the data.
  var cityCircle = new google.maps.Circle({
      strokeColor: RED,
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: RED,
      fillOpacity: 0.35,
      map: map,
      center: centreLatLng,
      radius: RADIUS_AREA
    });

}
