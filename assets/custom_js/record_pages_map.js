---
exclude_from_lunr: true
---
"use strict";
// Create a map for the record and generate a marker if the google-map-marker
// front matter variable is set to true.
function initRecordMap() {
  // HTML element for which the map will be generated under.
  var recordMapHTMLElement = document.getElementById("record_map");
  // Latitude value of the record.
  var recordLat = parseFloat(recordMapHTMLElement.getAttribute("record-lat"));
  // Longitude value of the record.
  var recordLng = parseFloat(recordMapHTMLElement.getAttribute("record-lng"));
  // Object that contains the latitude and longitude of the record.
  var latLng = { lat: recordLat, lng: recordLng };
  // Create a new map inside the recordMapHTMLElement.
  var map = new google.maps.Map(recordMapHTMLElement, {
    center: latLng,
    zoom: 8
  });
  // Create a marker that marks the location of the record if the google-map-marker
  // variable in the _config.yml file is set to true.
  if ("{{ site.data.additional_config.google-map-marker }}" == "true") {
    // Title of the record
    var recordTitle = recordMapHTMLElement.getAttribute("record-title");
    // Create a marker with the marker position specific to the record. The map
    // which is used to display the marker, and the title of the marker.
    var marker = new google.maps.Marker({
      position: latLng,
      map: map,
      title: recordTitle
    });
  }
}
