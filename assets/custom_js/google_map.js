---
---
function initHomePageMap() {

 var latLon = {lat: 42.6169, lng: 25.2848 };

 var map = new google.maps.Map(document.getElementById('homepagemap'),{
   center: latLon,
   zoom: 8
 });

 var centroidMarker = new google.maps.Marker({
    position: latLon,
    map: map,
    title: "Centroid"
  });

}
