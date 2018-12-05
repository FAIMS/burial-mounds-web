# Adding Additional Stylesheet or Javascript

Users wishing to add more additional styling to their website, please refer to the [adding additional stylesheet](#adding-additional-stylesheet) section. Users that wish to add more *Javascript* should refer to the [adding additional Javascript](#adding-additional-javascript) section in this document.

## Adding Additional Stylesheet

If users wish to add additional stylesheets, it is recommended that they create the css file in the *\_assets/custom_css* folder and link the stylesheet in the *additional\_head.html* file.

### Adding Additional Sass

If you are using sass, you can create scss files in the *\_sass* folder and then import the file in *assets/custom_css/custom_css.scss*. No additional linking other than importing it in is needed because the css generated from the sass file is already linked.

Please refer to [Jekyll official documentation regarding sass](https://jekyllrb.com/docs/assets/#sassscss) for more information.

## Adding Additional Javascript

In the *\_includes/helper* folder, there is a html file called *additional\_footer.html*, users are recommended to put additional javascript in this file. If users wish to add *Javascript* that uses liquid tags and variables then please add the *Javascript* code inside the file, enclosed within `<script>` tags. Alternatively, users can add the set of triple dashes at the top of their file, which will get Jekyll to process the file.

Below is the Javascript code that uses Google Maps API to generate maps for record for the Burial Mounds website which uses Javascript to get the values of the attributes `record-lat` and `record-lng` for the HTML element `record_map`. The values of these element is the latitude and longitude value of that particular record.

```javascript
---
exclude_from_lunr: true
---
// Create a map for the record and generate a marker if the google-map-marker
// front matter variable is set to true.
function initRecordMap() {
    // HTML element for which the map will be generated under.
    var recordMapHTMLElement = document.getElementById('record_map');
    // Latitude value of the record.
    var recordLat = parseFloat(recordMapHTMLElement.getAttribute("record-lat"));
    // Longitude value of the record.
    var recordLng = parseFloat(recordMapHTMLElement.getAttribute("record-lng"));
    // Object that contains the latitude and longitude of the record.
    var latLng = {lat: recordLat, lng: recordLng};
    // Create a new map inside the recordMapHTMLElement.
    var map = new google.maps.Map(recordMapHTMLElement, {
        center: latLng,
        zoom: 8
    });
    // Create a marker that marks the location of the record if the google-map-marker
    // variable in the _config.yml file is set to true.
    if('{{ site.data.additional_config.google-map-marker }}' == 'true'){
        // Title of the record
        var recordTitle = recordMapHTMLElement.getAttribute("record-title");
        // Create a marker with the marker position specific to the record. The map
        // which is used to display the marker, and the title of the marker.
        var marker = new google.maps.Marker({
            position: latLng,
            map: map,
            title: recordTitle});
    }
}
```

The HTML code before is the `div` element for the map and is located in *\_layouts/records.html* file.

```html
<div id="record_map" record-title='{{ page.title }}' record-lat='{{ page.latitude }}' record-lng='{{ page.longitude }}'></div>
```

The `div` have three attributes, namely, `record-title`, `record-lat` and `record-lng`, these store the front matter variables `title`, `latitude`, and `longitude` for that page.

Each page front matter will have variables with that name but possibly different value. For example, the Mound with TRAP ID 1001 have a latitude of 42.627103 and 25.246605 while the Mound with id 1002 have latitude 42.626585 and longitude 25.250297. So the _latitude_ value will be 42.627103 on the page for Mound with id 1001 and the _latitude_ value will be 42.626585 for the Mound with id 1002.

The triple dashes denotes the front matter, the values inside are the front matter variables and its values. In the code snippet above, there is one front matter variable called `exclude_from_lunr` which has the value *true*. One thing to note is that it is possible to have front matter but no values. This is done by triple dashes with the next line with only triple dashes.

```Javascript
---
---
// Create a map for the record and generate a marker if the google-map-marker
// front matter variable is set to true.
function initRecordMap() {
  // Code that create the map.
}
```
