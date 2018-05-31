---
exclude_from_lunr: true
---
'use strict'
function initHomePageMap() {
 var centreLatLng = {lat: 42.6169, lng: 25.2848 };

 var map = new google.maps.Map(document.getElementById('home_page_map'),{
   center: centreLatLng,
   zoom: 11
 });
  {% capture markers %}
  [
  {% for post in site.posts %}
  {"title":"{{ post.title }}","lat":"{{ post.latitude}}","lng":"{{ post.longitude }}"}
  {% if forloop.last %}{% else %},{% endif %}
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

  var cityCircle = new google.maps.Circle({
      strokeColor: '#FF0000',
      strokeOpacity: 0.8,
      strokeWeight: 2,
      fillColor: '#FF0000',
      fillOpacity: 0.35,
      map: map,
      center: centreLatLng,
      radius: 15*1000
    });

}
