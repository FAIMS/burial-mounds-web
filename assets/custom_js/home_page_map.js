---
exclude_from_lunr: true
---
'use strict'
function initHomePageMap() {
 var centreLatLng = {lat: 42.6169, lng: 25.2848 };

 var homePageMapHTMLElement = document.getElementById('home_page_map');
 var map = new google.maps.Map(homePageMapHTMLElement, {
   center: centreLatLng,
   zoom: 11
 });
  {% capture markers %}
  [
  {% for post in site.posts %}
  {"title":"{{ post.title }}","lat":"{{ post.latitude}}","lng":"{{ post.longitude }}"}
  {%- if forloop.last -%}{%- else -%},{%- endif -%}
  {% endfor %}
  ]
  {% endcapture %}
  var markers = {{markers | strip_newlines}};

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
