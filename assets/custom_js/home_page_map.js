---
exclude_from_lunr: true
---
function initHomePageMap() {

 var latLon = {lat: 42.6169, lng: 25.2848 };

 var map = new google.maps.Map(document.getElementById('home_page_map'),{
   center: latLon,
   zoom: 11
 });
  {% capture markers %}
  [
  {% for post in site.posts %}
  {"title" : "{{ post.title }}", "latitude" : "{{ post.latitude}}", "longitude" : "{{ post.longitude }}"}
  {% if forloop.last %}{% else %},{% endif %}
  {% endfor %}
  ]
  {% endcapture %}
  var markers = {{markers | strip_newlines}};
  for(var i = 0; i < markers.length; i++){
    var latLng = new google.maps.LatLng(markers[i].latitude, markers[i].longitude);
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
      center: latLon,
      radius: 15 * 1000
    });

}
