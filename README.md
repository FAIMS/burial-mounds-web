# Introduction
This is a template that uses [*Jekyll*](https://jekyllrb.com/) and based off [feeling-responsive](https://github.com/Phlow/feeling-responsive-v2) theme by Phlow.

The purpose of this project is to generate a data-driven website from a CSV. For the purpose of this project, each row in the CSV will be considered a `record`, and a page for each record will be called a `record page` and that a [*post*](https://jekyllrb.com/docs/posts/) in Jekyll is in our case a `record page`. The columns in the csv will be referred to as a `attribute`.

To get the basic structure, please follow the steps in this README. It is assumed that the user have basic knowledge of *Jekyll* if not, please refer to https://jekyllrb.com/docs/home/ for more information.

# Getting Started

This section will briefly discuss the process required to use this project to create a website.

1. Configuring the project such as the title of the project, the logo, navigation bar that appears at the top of the page. Refer to [configuration](#configuration) section for more information.
2. Using the *record.html* located inside the *\_layouts* folder as a template, work through the file and change it according to your requirements. Refer to the [record page template](#record-page-template) section for more information.
3. Auto generate record pages using the script provided. Refer to the [generating record pages](#generating-record-pages) section for more information.


# Software Prerequisites
To run the python scripts provided in the *\_import* folder, the user will need to have `Python 3.5.2` installed.

To test the website locally, the user will need to have `Jekyll` installed. It is also assumed that you are using `Ubuntu` operating system if you wish to test your website locally before uploading to Github Pages.

**NOTE**: If users do not have required Python Modules and attempt to run the Python scripts provided, they will receive errors, please install the required Python modules that are missing. Please refer to the [required Python module](#required-python-modules) section in regards to which modules is needed for the Python scripts provided.

Please refer to https://docs.python.org/3/installing/index.html if you need more information on Python modules and how to install Python modules.

## Required Python Modules
The required modules to run the Python scripts in *\_import* folder is in the `requirements.txt` file. Please download the modules listed in that file.

## Installing Jekyll
Please refer to [Jekyll offical documentation](https://jekyllrb.com/docs/installation/) for instructions to install Jekyll on your system.

If you are using a Windows system, please refer to the page regarding installing [Jekyll on Windows](https://jekyllrb.com/docs/installation/windows/).

### Running Jekyll Locally
Assuming jekyll is installed, to see your website locally, open up the terminal at the root of the folder of the project. Type in the following command then press enter

```
bundle exec jekyll serve --config _config.yml,_config_dev.yml
```

Another option is to run the shell script *local\_jekyll\_build.sh* located at the root path of this project.

# Configuration
The *\_config.yml* file contains configuration options for the website. For basic configuration, do the following steps.

1. Open the *\_config.yml* file and work through it.
    * The main front matter variables for basic customisation is:
        * *title*:
        * *slogan*
        * *descripton*
        * *credits*
        * *author*
        * *url*
        * *baseurl*
        * More details can be found on https://help.github.com/articles/configuring-jekyll/ and https://jekyllrb.com/docs/configuration/.

	* **NOTE**: If you are running jekyll locally to see your changes, please stop the server then run it again to see changes made in your *\_config.yml* file
	* If the user wish to add more custom data that can be accessed throughout the site via the Liquid templating system, then rather adding it directly into *\_config.yml* file, users are recommended to add it into the *additional\_config.yml* file which is located in the *\_data* folder.
	* For example the variable *google-map-marker* can be accessed via `site.data.additional_config.google-map-marker`.
	* More information is contained here: https://jekyllrb.com/docs/datafiles/

2. Add your *logo.png* (if you have one) to */assets/img/*.

3. Open *\_data/socialmedia.yml* and add your own social media links.

4. Open *\_data/navigation.yml* and customize your navigation.
	A navigation link composed of components, *title*, *url*, *side*.
	*title* is the name of the link
	*url* is the relative link to the page.		
  *side* is whether the link would be located on the left-hand or right-hand side of the navigation bar. It is recommended to put it all in the left hand side to keep the *Search* bar at its current location.

5. Open *\_data/language.yml* and translate the theme if necessary.

6. Open *\_data/services.yml* and customize links in the footer.

7. Open *\_data/network.yml* and customize links in the footer.

8. Open *\_data/authors.yml* and edit author information and set default author in config.yml.

## Adding Categories
The `categories` front matter variable is used to group records by tabs in the Collections page.


# Structure of the Project
This section will explain the structure of the project and decribe the top-level folders for the project:

* _assets_ folder contain the CSS, Javascript used in the project and also images that is used for the site such as the logo and default images for records.
* *\_data* contains the configuration YAML files for the project.
* *\_images* folder contains the images used in the site.
* *\_import* contains scripts to auto generate record pages from a CSV.
* *\_includes* contains content that can included into files.
* *\_pages* contains pages of the website
* *\_posts* contains the YML files for the record pages
* *\_sass* contains sass partials of our project.
* *\_site* contains the generated site that Jekyll outputs. This folder is added into `.gitignore` file.


# Preprocessing
Before auto generating record pages, ensure your data is well-formed for minimal hassle. A record should have a column that contains the unique identifer for that record.

## Preprocessing for Adding Images
While it is possible to manually link the images to a Record Page, there are two other ways to link images to a Record Page.

  1. Link local images to Record Pages using the Python script *local_images.py* in the *\_import* folder. Please see the [preprocessing required for linking local images section](#preprocessing-required-for-linking-local-images) for more information.
  2. Read a CSV that contains Google Drive links to images for Records and write it to the associated Record Page using the *google_drive.py* Python script in the *\_import* folder.

### File type for images
Please ensure your images are one of the following types so that the script is able to recognise the file as images:

  1. `.png`
  2. `.jpg`
  3. `.jpeg`

### Preprocessing Required for Linking Local Images
First, please ensure your files are of the types discussed in the [file type section](#file-type-for-images). On the root folder of the project, create a folder called `images` if it doesn't exist yet. Inside the `images` folder, group the images by the unique identifer of the record. For each folder, create a new folder inside the `images` folder with the name matching the unique identifer for that record.

**Example**:

For example, given a record with the unique id `1000` and the user wants to have the following images associated with that record:

  * `1000_Detail_Profile_of_RT.JPG`
  * `1000_Detail_RT2.JPG`
  * `1000_Large_RT.JPG`
  * `1000_Large_RT_Scale.JPG`
  * `1000_Overview_S.JPG`
  * `1000_Overview_year2009.JPG`
  * `1000_RT.JPG`

Then the user will need to create a new folder with the name `1000` and put all those images inside that folder. The below structure is the result.

```
images/
├── 1000
│   ├── 1000_Detail_Profile_of_RT.JPG
│   ├── 1000_Detail_RT2.JPG
│   ├── 1000_Large_RT.JPG
│   ├── 1000_Large_RT_Scale.JPG
│   ├── 1000_Overview_S.JPG
│   ├── 1000_Overview_year2009.JPG
│   ├── 1000_RT.JPG
```


### Images on google drive
There are requirements to use the provided `google_drive.py` Python script to link the image to its record. Please ensure that the id of the record is appended in the name of the image. To use the `google_drive.py`, the unique identifier should be uniform in length.

# Customization
Before auto generating record pages, the user can customize the site. This section will discuss some customisations available to the user

## Editing Record Pages Template

The record pages uses *\_layout/record.html* as the template, to modify the template, please see the [Components of the record page template section](#components-of-the-record-page-template)

## Merging Two CSV Together
A python script written in Python3 have been provided to merge two csv file based on a key.

## Map Functionality for Records
The map functionality for records is split into several components:

1. The `div` element with the id `record_map` is located in the *record.html* file inside the *\_layouts* folder. That div have 3 attributes which stores the title, latitude and longitude of that record.
2. The CSS required for the styling of the `div` element which is in the sass file *\_google\_maps.scss*.
3. The Javascript function that uses the Maps Javascript API. This is located in the *\_custom_js/record\_pages\_map.js* and importing that script is located in the *\_includes/additional\_helper/additional\_footer.html* file.

The default setting for the Map functionality is that it uses the `latitude` and `longitude` front matter variables of the record page. So if users wish to have a map, the column name in the csv must also correspond to that name.

**NOTE**: It is fine in the CSV to have the column name "Latitude" and "Longitude" because the script that generate a page for each row then converts the column names to lowercase when it passes it into the Front Matter for the record page.
  * **IMPORTANT**: The format of the coordinates should also be in *decimal degrees* which is what Google Map API uses.

### Markers for Record Maps
The `google-map-marker` variable is in the *additional\_config.yml* file and is used to determine whether to add a marker that points to the location of the record, if the user do not wish to have a Google Map marker then the user can edit the `google-map-marker` variable and change the value from *true* to *false* and if they wish to have the marker back then they would reverse it, changing the value from *false* to *true*.

#### Title of the Markers for Record Maps

The `title` front matter variable in the record page is used as the title of the Google Map marker.

## Adding Additional Metadata Inside the &lt;head&gt; Tag
In the *\_includes/helper* folder, there is a HTML file called *head.html*, this contains all the default information about the page inside the `<head>` tags, another file named *additional\_head.html* file which is located in the *\_includes/addition\_helper* folder.

If the user want to add additional information that they want enclosed inside the `<head>` tag of the website, it is recommended to add it into the *additional\_head.html* file so that there is no confusion between the default metadata for the template and the new metadata defined by the user, the additional metadata added will be after the default metadata because we are using jekyll `include` tag to include the content from *additional\_head.html* into the *head.html* file. However, the user is free to modify the *head.html* file.

## Adding Additional Stylesheet or Javascript
Users wishing to add more additional styling to their website, please refer to the [adding additional stylesheet](#adding-additional-stylesheet) section. Users that wish to add more *Javascript* should refer to the [adding additional Javascript](#adding-additional-javascript) section in this README.

### Adding Additional Stylesheet
If users wish to add additional stylesheets, it is recommended that they create the css file in the *\_assets/custom_css* folder and link the stylesheet in the *additional\_head.html* file.

#### Adding Additional Sass
If you are using sass, you can create scss files in the *\_sass* folder and then import the file in *assets/custom_css/custom_css.scss*. No additional linking other than importing it in is needed because the css generated from the sass file is already linked.

Please refer to https://jekyllrb.com/docs/assets/#sassscss for more information.

### Adding Additional Javascript
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

## Search Functionality
The current search function allows the user to search records by `title` and `record_id` variables. If users wish to customize their search, please read https://learn.cloudcannon.com/jekyll/jekyll-search-using-lunr-js/ which is used as a template for our project.

* _pages/search.md_ is the file which contains the search data.
* _assets/js/search.js_ is the file which contains the Javascript logic to perform the search.

## Excluding Files from Search

To explicitly exclude a page from search result. Please add `exclude_from_lunr` variable to the page YAML front matter and set that to `true` with no surrounding quotes, that means, `"true"` or `'true'` is not correct.

**Example: Correct value**

```yml
exclude_from_lunr: true
```

**Example: Incorrect values**

```yml
exclude_from_lunr: "true"
```

```yml
exclude_from_lunr: 'true'
```

## Adding Images for a Record Page
It is possible to link images to a associated Record Page.


## Photo Gallery for Records
The photo gallery is implementing using [slick](http://kenwheeler.github.io/slick/). There is two photo gallery in a record page, one is photo gallery used to display photos for that record and the second photo gallery is used as a navigation. The implmenetation is split into three parts:

1. The HTML structure is defined in the template html for the records, which by default is in *\_layouts/record.html*.
2. The CSS that is used to style the photo gallery such as the the navigation buttons for the photo gallery is in *assets/slick/slick-theme.css*.
3. The Javascript is used to defined the logic of the photo gallery is in *assets/custom_js/slick-settings.js*.

## Recompile Changes
Because this is a static website, everytime users wish to make push their changes (assuming the website is on Github):

1. Delete the *\_posts* folder
2. Recompile the record pages by running the *makeSite.py* Python script and additional scripts if needed
3. `git add` then `git commit` then `git push` to the remote repo


# Important Pages

## Collections

The *\_pages/pages-root-folder/collections.md* is the web page that is used to display the links to all the record pages. The organization of the pages is grouped by *categories* where one tab correspond to a category. A record page can appear in one or more category. To add a record page to belong to a category, add the name of the category in the YAML list for that record page under the *categories* key.

If user wish to change the content of the page, they can edit *\_pages/pages-root-folder/collections.md*.

## Record Page Template

The yaml template for record pages is the *\_import/template.yaml* file. The script that will generate record pages will use that as a template for the record pages.
The layout file that *\_import/template.yaml* uses is the *\_layout/record.html* file.

### Components of the Record Page Template

![Overview of record page](README_screenshots/record_page_overview.png)



# Generating Record Pages
In the *\_import* folder there is a Python script named *makeSite.py*. The purpose of the script is to generate a seperate yaml file for each row in the csv. Each column corresponds to a front matter variable in the yaml file. The variable will be the name of the column with all space characters replaced with the '\_' character and the characters are coverted to all lowercase (**EXCEPT** the unique identifer) .

**NOTE**: The unique identifier will be stored into the front matter variable `record_id`. You would need to provide the column name (case-sensitive) so that the script can extract the id for the record.

**Example**

In a csv file with 3 columns, '_TRAP ID_', '_Max diameter_', '_Surrounding Land Use_' and the values are, 1000, 34, "Annual Agriculture" for a row. then in the corresponding record page for that row, the front matter variable will be in the following format and we choose '_TRAP ID_' as the `record_id`, then the following code snippet will be the result.

```yml
record_id: '1000'
max_diameter: '34'
surrounding_land_use: Annual Agriculture
```
