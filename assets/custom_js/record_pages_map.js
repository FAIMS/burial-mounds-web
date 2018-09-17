---
exclude_from_lunr: true
---
'use strict';
function initMap() {
	var recordMapHTMLElement = document.getElementById('record_map');
	var recordLat = parseFloat(recordMapHTMLElement.getAttribute("record-lat"));
	var recordLng = parseFloat(recordMapHTMLElement.getAttribute("record-lng"));

	var latLng = {lat: recordLat, lng: recordLng};

	var map = new google.maps.Map(recordMapHTMLElement, {
		center: latLng,
		zoom: 8
	});
	
	if('{{ site.data.additional_config.google-map-marker }}' == 'true'){
		var marker = new google.maps.Marker({
		  position: latLng,
		  map: map,
		  title: recordMapHTMLElement.getAttribute("record-title")
		});
	}
}
