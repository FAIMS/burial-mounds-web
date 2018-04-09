# Introduction
This is a template that uses Jekyll and based off feeling-responsive theme by Phlow. To get the basic structure, please follow the steps in this README. It is assumed that the user have basic knowledge of jekyll, if not, please refer to https://jekyllrb.com/docs/home/ for more information. The purpose of this project is to generate a data-driven website from a CSV. For the purpose of this project, each row in the CSV will be considered a _record_ and a page for each record will be called a _Record Page_.

## Prerequisites
Need to have Python installed to run the script and also have Jekyll installed to test the website locally.

## Configuration
The \__config.yml_ file contains configuration options for the website. For basic configuration, do the following steps.

1. Open the \__config.yml_ file and work through it. The main key:value pair to worry about for basic customisation is _title_, _slogan_, _descripton_, _credits_, _author_, _url_, _baseurl_. More details can be found on https://help.github.com/articles/configuring-jekyll/ and https://jekyllrb.com/docs/configuration/.

2. Add your _logo.png_ (if you have one) to _/assets/img/_.

3. Open \__data/socialmedia.yml_ and add your own social media links.

4. Open \__data/navigation.yml_ and customize your navigation.
	A navigation link composed of components, _title_, _url_, _side_.
	_title_ is the name of the link
	_url_ is the relative link to the page.		
	_side_ is whether the link would be located on the left-hand or right-hand side of the navigation bar. It is recommended to put it all in the left hand side to keep the *Search* bar at its current location.

5. Open \__data/language.yml_ and translate the theme if necessary.

6. Open \__data/services.yml_ and customize links in the footer.

7. Open \__data/network.yml_ and customize links in the footer.

8. Open \__data/authors.yml_ and edit author information and set default author in config.yml.


	* Addtion scss files can be made in the \__sass_ folder. You need then need to import the file in assets/css/styles_feeling_response.scss, for it to be included in the future build. For example, if you make a sass file called _tabs.scss_ in the \__sass_ folder then, inside the assets/css/styles_feeling_response.scss file, you would write 

```
@import  
```

## Merging two csv together
A python script written in python3 have been provided to merge two csv file based on a key.

## Auto-generate page for each row
In the _\_import_ folder there is a script that have been provided. The purpose of the script is to generate a seperate yaml file for each row in the csv. Each column correspond to a _key:value_ pair in the yaml file, the key is name of the column with all space characters replaced with the '_' character and the characters are coverted to all lowercase.

Dependencies required:
ruamel.yaml




## Map functionality
The javascript required for the google map functionality for each Record page is located \_includes/helper/footer\_scripts.html file. It uses Liquid templating and only apply the javascript for Record Pages. In the front matter for the Record Pages, there is a collection variable called *maps* that have two key:value pairs, *lat* and *lon*, these correspond to the latitude and longitude for that Record. 

To activate the map for that record, the variable variable need to exist and the *lat* and *lon* must have a value so the map will be centered according to the value given. If the collection variable *maps* does not exist, the *Map* tab for the record page will not be available.
