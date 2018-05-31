---
exclude_from_lunr: true
---
'use strict';
function initMap() {
	var latLng = {lat: parseFloat(document.getElementById('record_map').getAttribute("record-lat")),
 			lng: parseFloat(document.getElementById('record_map').getAttribute("record-lng"))};

	var map = new google.maps.Map(document.getElementById('record_map'),{
		center: latLng,
		zoom: 8
	});
	if('{{ site.data.additional_config.google-map-marker }}' == 'true'){
		var marker = new google.maps.Marker({
		  position: latLng,
		  map: map,
		  title: document.getElementById('record_map').getAttribute("record-title")
		});
	}
}
