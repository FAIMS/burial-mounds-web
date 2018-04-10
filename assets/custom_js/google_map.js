---
---
function initMap() {
 console.log(parseFloat('{{ page.latitude }}'));
 var latLon = {lat: parseFloat('{{ page.latitude }}'), lng: parseFloat('{{ page.longitude}}')};

 var map = new google.maps.Map(document.getElementById('map'),{
   center: latLon,
   zoom: 8
 });

 var marker = new google.maps.Marker({
    position: latLon,
    map: map,
    title: '{{ page.title}}'
  });
}
