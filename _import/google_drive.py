#!/usr/bin/env python3
"""This module reads from a csv that contains url to images located on
Google Drive. and stores the urls on the respective record list variable
`images`."""

import csv
import os
from ruamel.yaml import YAML

import util as UTIL
from consts import FOLDER, ID_FRONT_MATTER_VARIABLE_NAME, KEY_FOR_FIRST_IMG

SHEET = "BM-Pic.csv"
DEST = "../_posts"

# Name of the collection of the Records Pages
COLLECTION_NAME = "TRAP Mounds"

# Objects is the list of rows from the csv that contains the url of the images
OBJECTS = []
CSV_HEADINGS = []
RECORD_DICT = {}
with open(SHEET, newline='') as csvfile:
    SHEETREADER = csv.DictReader(csvfile)
    CSV_HEADINGS = SHEETREADER.fieldnames
    for row in SHEETREADER:
        OBJECTS.append(row)

# Length of the uuid
KEY_LEN = 4

STR_TO_REMOVE = "https://drive.google.com/file/d/"

PREPEND_LINK = "https://drive.google.com/uc?id="

print("APPENDING")
for row in OBJECTS:
    image_name = row['Name']
    # Get the uuid that correspond for that image
    record_id = image_name[:KEY_LEN]
    # Preprocessing
    # url is the string that is the url to the image
    url = row['URL'].replace(STR_TO_REMOVE, "")
    url = url.replace("/view?usp=drivesdk", "")
    # If first image then create a empty list first
    if record_id not in RECORD_DICT:
        RECORD_DICT[record_id] = []

    url = PREPEND_LINK + url
    entry = {'Name': image_name, 'URL': url}
    # If there is Overview in the image name then place it at the front of the list
    # for the record with id record_id
    if KEY_FOR_FIRST_IMG in image_name:
        RECORD_DICT[record_id].insert(0, entry)
    else:
        RECORD_DICT[record_id].append(entry)

if os.path.exists(FOLDER):
    # For each Record Page in folder
    for file in os.listdir(FOLDER):
        yaml = YAML()
        file_name = os.fsdecode(file)
        record_page_path = FOLDER + file_name
        record_page_lines = open(record_page_path).readlines()
        open(record_page_path, 'w').writelines(record_page_lines[1:-1])
        with open(record_page_path) as record_page:
            objyaml = yaml.load(record_page.read())
            record_id = objyaml[ID_FRONT_MATTER_VARIABLE_NAME]
            if 'images' not in objyaml:
                objyaml['images'] = []
            if record_id in RECORD_DICT:
                for row in RECORD_DICT[record_id]:
                    item = {'image_path': row['URL'], 'title': row['Name']}
                    UTIL.insert_image_link_into_list(
                        objyaml['images'], item, row['Name'], KEY_FOR_FIRST_IMG)
            if not objyaml['images']:
                objyaml.pop('images', None)
            UTIL.dump(record_page_path, yaml, objyaml)
print("FINISH")
