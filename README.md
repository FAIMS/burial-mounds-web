# README <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Software Prerequisites](#software-prerequisites)
  - [Required Python Modules](#required-python-modules)
  - [Installing Jekyll](#installing-jekyll)
    - [Running Jekyll Locally](#running-jekyll-locally)
- [Configuration](#configuration)
  - [Adding Categories](#adding-categories)
- [Structure of the Project](#structure-of-the-project)
- [Preprocessing](#preprocessing)
  - [Preprocessing for Adding Images](#preprocessing-for-adding-images)
    - [File type for images](#file-type-for-images)
  - [Preprocessing Required for Linking Local Images](#preprocessing-required-for-linking-local-images)
  - [Preprocessing Required for Images on Google Drive](#preprocessing-required-for-images-on-google-drive)
- [Customization](#customization)
  - [Editing Record Pages Template](#editing-record-pages-template)
  - [Merging Two CSV Together](#merging-two-csv-together)
  - [Map Functionality for Records](#map-functionality-for-records)
    - [Markers for Record Maps](#markers-for-record-maps)
    - [Title of the Markers for Record Maps](#title-of-the-markers-for-record-maps)
  - [Adding Additional Metadata Inside the HTML head Tag](#adding-additional-metadata-inside-the-html-head-tag)
  - [Adding Additional Stylesheet or Javascript](#adding-additional-stylesheet-or-javascript)
  - [Search Functionality](#search-functionality)
  - [Excluding Files from Search](#excluding-files-from-search)
  - [Adding Images for a Record Page from Local Source](#adding-images-for-a-record-page-from-local-source)
  - [Adding Images for a Record Page from Google Drive](#adding-images-for-a-record-page-from-google-drive)
  - [Photo Gallery for Records](#photo-gallery-for-records)
  - [Recompile Changes](#recompile-changes)
- [Important Pages](#important-pages)
  - [Collections](#collections)
  - [Record Page Template](#record-page-template)
    - [Components of the Record Page Template](#components-of-the-record-page-template)
- [Generating Record Pages](#generating-record-pages)
- [Record Page](#record-page)

## Introduction

This is a template uses [*Jekyll*](https://jekyllrb.com/) and based off [feeling-responsive](https://github.com/Phlow/feeling-responsive-v2) theme by Phlow.

The purpose of this project is to generate a data-driven website from a CSV. For the purpose of this project, each row in the CSV will be considered a `record`, and a page for each record will be called a `record page` and that a [*post*](https://jekyllrb.com/docs/posts/) in Jekyll is in our case a `record page`. The column in the csv will be referred to as a `attribute`.

To get the basic structure, please follow the steps in this README. It is assumed that the user have basic knowledge of *Jekyll* if not, please refer to https://jekyllrb.com/docs/home/ for more information.

## Getting Started

This section will briefly discuss the process required to use this project to create a website.

1. Configuring the project such as the title of the project, the logo, navigation bar that appears at the top of the page. Refer to [configuration](#configuration) section for more information.
2. Using the *record.html* located inside the *\_layouts* folder as a template, work through the file and change it according to your requirements. Refer to the [record page template](#record-page-template) section for more information.
3. Auto generate record pages using the script provided. Refer to the [generating record pages](#generating-record-pages) section for more information.

## Software Prerequisites

To run the python scripts provided in the *\_import* folder, the user will need to have `Python 3.5.2` installed.

To test the website locally, the user will need to have `Jekyll` installed. It is also assumed that you are using `Ubuntu` operating system if you wish to test your website locally before uploading to Github Pages.

**NOTE**: If users do not have required Python Modules and attempt to run the Python scripts provided, they will receive errors, please install the required Python modules that are missing. Please refer to the [required Python module](#required-python-modules) section in regards to which modules is needed for the Python scripts provided.

Please refer to https://docs.python.org/3/installing/index.html if you need more information on Python modules and how to install Python modules.

[Back to TOC](#table-of-contents)

### Required Python Modules

The required modules to run the Python scripts in *\_import* folder is in the `requirements.txt` file. Please download the modules listed in that file.

[Back to TOC](#table-of-contents)

### Installing Jekyll

Please refer to [Jekyll offical documentation](https://jekyllrb.com/docs/installation/) for instructions to install Jekyll on your system.

If you are using a Windows system, please refer to the page regarding installing [Jekyll on Windows](https://jekyllrb.com/docs/installation/windows/).

#### Running Jekyll Locally

Assuming jekyll is installed, to see your website locally, open up the terminal at the root of the folder of the project. Type in the following command then press enter

```bash
bundle exec jekyll serve --config _config.yml,_config_dev.yml
```

Another option is to run the shell script *local\_jekyll\_build.sh* located at the root path of this project.

[Back to TOC](#table-of-contents)

## Configuration

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
        * More details can be found on <https://help.github.com/articles/configuring-jekyll/> and https://jekyllrb.com/docs/configuration/.

    * **NOTE**: If you are running jekyll locally to see your changes, please stop the server then run it again to see changes made in your *\_config.yml* file
    * If the user wish to add more custom data that can be accessed throughout the site via the Liquid templating system, then rather adding it directly into *\_config.yml* file, users are recommended to add it into the *additional\_config.yml* file which is located in the *\_data* folder.
    * For example the variable *google-map-marker* can be accessed via `site.data.additional_config.google-map-marker`.
    * More information is contained here: <https://jekyllrb.com/docs/datafiles/>

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

[Back to TOC](#table-of-contents)

### Adding Categories

The `categories` front matter variable is used to group records by tabs in the Collections page.

[Back to TOC](#table-of-contents)

## Structure of the Project

This section will explain the structure of the project and decribe the top-level folders for the project:

* _assets_ folder contain the CSS, Javascript used in the project and also images that is used for the site such as the logo and default images for records.
* *\_data* contains the configuration YAML files for the project.
* *\_images* folder contains the images used in the site.
* *\_import* contains scripts to generate record pages from a CSV, link images to associated Record Page. CSV needed to use those scripts.
* *\_includes* contains content that can included into files.
* *\_pages* contains pages of the website
* *\_posts* contains the YML files for the record pages
* *\_sass* contains sass partials of our project.
* *\_site* contains the generated site that Jekyll outputs. This folder is added into `.gitignore` file.

[Back to TOC](#table-of-contents)

## Preprocessing

Before auto generating record pages, ensure your data is well-formed for minimal hassle. A record should have a column that contains the unique identifer for that record.

[Back to TOC](#table-of-contents)

### Preprocessing for Adding Images

While it is possible to manually link the images to a Record Page, there are two other ways to link images to a Record Page.

  1. Link local images to Record Pages using the Python script *local_images.py* in the *\_import* folder. Please see the [preprocessing required for linking local images section](#preprocessing-required-for-linking-local-images) for more information.
  2. Read a CSV that contains Google Drive links to images for Records and write it to the associated Record Page using the *google_drive.py* Python script in the *\_import* folder.

[Back to TOC](#table-of-contents)

#### File type for images

Please ensure your images are one of the following types so that the script is able to recognise the file as images:

  1. `.png`
  2. `.jpg`
  3. `.jpeg`

[Back to TOC](#table-of-contents)

### Preprocessing Required for Linking Local Images

First, please ensure your files are of the types discussed in the [file type section](#file-type-for-images), otherwise, please convert your image to one of the file type discussed in that discussion.

On the root folder of the project, create a folder called `images` if it doesn't exist yet. Inside the `images` folder, group the images by the unique identifer of the record. For each folder, create a new folder inside the `images` folder with the name matching the unique identifer for that record.

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

```bash
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

[Back to TOC](#table-of-contents)

### Preprocessing Required for Images on Google Drive

First, please ensure your files are of the types discussed in the [file type section](#file-type-for-images), otherwise, please convert your image to one of the file type discussed in that discussion.

To use the provided `google_drive.py` Python script. The url of the Google Drive images will need to be extracted into a CSV. The script assumes that the length of the unique identifier is uniform, and that the unique identifier of appended in the name of the file.

**Example**

Assume a record with the unique identifer of `1000` and it have 3 images associated with it:

* `image-one.jpg`
* `image-two.jpg`
* `image-three.jpg`

User will then append `1000` to the filename of those images:

* `1000_image-one.jpg`
* `1000_image-two.jpg`
* `1000_image-three.jpg`

[Back to TOC](#table-of-contents)

## Customization

Before auto generating record pages, the user can customize the site. This section will discuss some customisations available to the user.

[Back to TOC](#table-of-contents)

### Editing Record Pages Template

The record pages uses *\_layout/record.html* as the template, to modify the template, please see the [Components of the record page template section](#components-of-the-record-page-template)

[Back to TOC](#table-of-contents)

### Merging Two CSV Together

A python script written in Python3 have been provided to merge two csv file based on a key.

[Back to TOC](#table-of-contents)

### Map Functionality for Records

The map functionality for records is split into several components:

1. The `div` element with the id `record_map` is located in the *record.html* file inside the *\_layouts* folder. That div have 3 attributes which stores the title, latitude and longitude of that record.
2. The CSS required for the styling of the `div` element which is in the sass file *\_google\_maps.scss*.
3. The Javascript function that uses the Maps Javascript API. This is located in the *\_custom_js/record\_pages\_map.js* and importing that script is located in the *\_includes/additional\_helper/additional\_footer.html* file.

The default setting for the Map functionality is that it uses the `latitude` and `longitude` front matter variables of the record page. So if users wish to have a map, the column name in the csv must also correspond to that name.

**NOTE**: It is fine in the CSV to have the column name "Latitude" and "Longitude" because the script that generate a page for each row then converts the column names to lowercase when it passes it into the Front Matter for the record page.
  * **IMPORTANT**: The format of the coordinates should also be in *decimal degrees* which is what Google Map API uses.

[Back to TOC](#table-of-contents)

#### Markers for Record Maps

The `google-map-marker` variable is in the *additional\_config.yml* file and is used to determine whether to add a marker that points to the location of the record, if the user do not wish to have a Google Map marker then the user can edit the `google-map-marker` variable and change the value from *true* to *false* and if they wish to have the marker back then they would reverse it, changing the value from *false* to *true*.

[Back to TOC](#table-of-contents)

#### Title of the Markers for Record Maps

The `title` front matter variable in the record page is used as the title of the Google Map marker.

[Back to TOC](#table-of-contents)

### Adding Additional Metadata Inside the HTML head Tag

In the *\_includes/helper* folder, there is a HTML file called *head.html*, this contains all the default information about the page inside the `<head>` tags, another file named *additional\_head.html* file which is located in the *\_includes/addition\_helper* folder.

If the user want to add additional information that they want enclosed inside the `<head>` tag of the website, it is recommended to add it into the *additional\_head.html* file so that there is no confusion between the default metadata for the template and the new metadata defined by the user, the additional metadata added will be after the default metadata because we are using jekyll `include` tag to include the content from *additional\_head.html* into the *head.html* file. However, the user is free to modify the *head.html* file.

[Back to TOC](#table-of-contents)

### Adding Additional Stylesheet or Javascript

For users that wish to customise the styling and behaviour of their website by adding additional stylesheet or Javscript, please refer to the [additional additional javascript or stylesheet document](adding-additional-javascript-or-stylesheet.md) for more information.

[Back to TOC](#table-of-contents)

### Search Functionality

The current search function allows the user to search records by `title` and `record_id` variables. If users wish to customize their search, please read https://learn.cloudcannon.com/jekyll/jekyll-search-using-lunr-js/ which is used as a template for our project.

* _pages/search.md_ is the file which contains the search data.
* _assets/js/search.js_ is the file which contains the Javascript logic to perform the search.

[Back to TOC](#table-of-contents)

### Excluding Files from Search

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

[Back to TOC](#table-of-contents)

### Adding Images for a Record Page from Local Source

Please ensure to read and follow the instructions provided in the [preprocessing required for linking local images section](#preprocessing-required-for-linking-local-images) before proceeding with this section.

Once you done with that, please follow the following steps:

  1. If you have run the `make_site.py` Python script to generate the Record Pages, then you can skip this step and move onto step 4, otherwise, please read the [generating record pages section](#generating-record-pages) and follow the instructions in that section.
  2. Run the `local_images.py` Python script. Once that is done, you have finish linking images from the `images/` folder to its associated Record Page.

Once you have finish all the steps, run the website to test if the images were successfully associated with the Record Page.  

[Back to TOC](#table-of-contents)

### Adding Images for a Record Page from Google Drive

Please ensure to read the [generating google drive link to csv page](_import/generating-google-drive-link-csv.md) to generate the CSV that contains the Google Drive CSV.

Once you have the generated CSV, please follow the following steps:

  1. Ensure that the CSV file is in the **\_import** folder.
  2. Ensure the value for the key `csv_file_name` in [customizable-variables.yaml](_import/customizable-variables.yaml) is the same as the file name of the CSV.
  3. If you have run the `make_site.py` Python script to generate the Record Pages, then you can skip this step and move onto step 4, otherwise, please read the [generating record pages section](#generating-record-pages) and follow the instructions in that section.
  4. Run the `google_drive.py` Python script. Once that is done, you have finish adding images from Google Drive.

Once you have finish all the steps, run the website to test if the images were successfully associated with the Record Page.

[Back to TOC](#table-of-contents)

### Photo Gallery for Records

The photo gallery is implementing using [slick](http://kenwheeler.github.io/slick/). There is two photo gallery in a record page, one is photo gallery used to display photos for that record and the second photo gallery is used as a navigation. The implmenetation is split into three parts:

1. The HTML structure is defined in the template html for the records, which by default is in *\_layouts/record.html*.
2. The CSS that is used to style the photo gallery such as the the navigation buttons for the photo gallery is in *assets/slick/slick-theme.css*.
3. The Javascript is used to defined the logic of the photo gallery is in *assets/custom_js/slick-settings.js*.

[Back to TOC](#table-of-contents)

### Recompile Changes

Because this is a static website, everytime users wish to make push their changes (assuming the website is on Github):

1. Delete the *\_posts* folder
2. Recompile the record pages by running the *makeSite.py* Python script and additional scripts if needed
3. `git add` then `git commit` then `git push` to the remote repo

[Back to TOC](#table-of-contents)

## Important Pages

### Collections

The *\_pages/pages-root-folder/collections.md* is the web page that is used to display the links to all the record pages. The organization of the pages is grouped by *categories* where one tab correspond to a category. A record page can appear in one or more category. To add a record page to belong to a category, add the name of the category in the YAML list for that record page under the *categories* key.

If user wish to change the content of the page, they can edit *\_pages/pages-root-folder/collections.md*.

[Back to TOC](#table-of-contents)

### Record Page Template

The yaml template for record pages is the *\_import/template.yaml* file. The script that will generate record pages will use that as a template for the record pages.
The layout file that *\_import/template.yaml* uses is the *\_layout/record.html* file.

[Back to TOC](#table-of-contents)

#### Components of the Record Page Template

![Overview of record page](README_screenshots/record_page_overview.png)

[Back to TOC](#table-of-contents)

## Generating Record Pages

In the *\_import* folder there is a Python script named *makeSite.py*. The purpose of the script is to generate a seperate yaml file for each row in the csv. Each column corresponds to a front matter variable in the yaml file. The variable will be the name of the column with all space characters replaced with the '\_' character and the characters are coverted to all lowercase (**EXCEPT** the unique identifer) .

**NOTE**: The unique identifier will be stored into the front matter variable `record_id`. You would need to provide the column name (case-sensitive) so that the script can extract the id for the record.

**Example**

In a csv file with 3 columns, '_TRAP ID_', '_Max diameter_', '_Surrounding Land Use_' and the values are, 1000, 34, "Annual Agriculture" for a row. then in the corresponding record page for that row, the front matter variable will be in the following format and we choose '_TRAP ID_' as the `record_id`, then the following code snippet will be the result.

```yml
record_id: '1000'
max_diameter: '34'
surrounding_land_use: Annual Agriculture
```

[Back to TOC](#table-of-contents)

## Record Page

A record page is a page in the *\_post* folder. It contains front matter variables which stores the attributes of that record. The front matter variables are enclosed between triple dashes lines.

Here is a simple example:

```YML
---
layout: record
title: TRAP Mound - 1000

record_id: '1000'
---
```

In the example above, there are three front matter variable, namely, `layout`, `title`, and `record_id`. The front matter variables are used by the template to display data specific to that Record.

**NOTE**: The front matter variables must be the first thing in the file.

[Back to TOC](#table-of-contents)
