#!/usr/bin/env python3
"""This module reads from a csv that contains url to images located on
Google Drive. and stores the urls on the respective record list variable
`images`."""

import csv
import os
from ruamel.yaml import YAML

import util as UTIL
from consts import FOLDER, ID_FRONT_MATTER_VARIABLE_NAME, KEY_FOR_FIRST_IMG, \
    IMAGES_FRONT_MATTER_VARIABLE_NAME, KEY_LEN

SHEET = "BM-Pic.csv"
DEST = "../_posts"

# Name of the collection of the Records Pages.
COLLECTION_NAME = "TRAP Mounds"

# Objects is the list of rows from the csv that contains the url of the images.
OBJECTS = []
CSV_HEADINGS = []
# Dictionary that maps a record id to a list of dict, where each dict contains
# the name of the image and the Google Drive link.
RECORD_DICT = {}
# Read the CSV file that contains the links and store that into OBJECTS
with open(SHEET, newline='') as csvfile:
    SHEETREADER = csv.DictReader(csvfile)
    CSV_HEADINGS = SHEETREADER.fieldnames
    for row in SHEETREADER:
        OBJECTS.append(row)

# Strings to be removed, and replaced with the url so that it can be
# linked via a website.
GOOGLE_DRIVE_VIEW_FILE_STR = "https://drive.google.com/file/d/"
GOOGLE_DRIVE_VIEW_SDK_STR = "/view?usp=drivesdk"

print("APPENDING")

# Iterate through OBJECTS and populate RECORD_DICT.
for row in OBJECTS:
    view_link = "https://drive.google.com/uc?id={file_id}"
    image_name = row['Name']
    # Get the uuid that correspond for that image
    record_id = image_name[:KEY_LEN]
    # Preprocessing
    # google_drive_image_file_id is the file id
    # for that image on google drive
    google_drive_image_file_id = row['URL'].replace(
        GOOGLE_DRIVE_VIEW_FILE_STR, "")
    google_drive_image_file_id = google_drive_image_file_id.replace(
        GOOGLE_DRIVE_VIEW_SDK_STR, "")
    # If first image then create a empty list first
    if record_id not in RECORD_DICT:
        RECORD_DICT[record_id] = []

    url = view_link.format(file_id=google_drive_image_file_id)
    entry = {'Name': image_name, 'URL': url}
    # If there is Overview in the image name then place it at the front of the list
    # for the record with id record_id
    UTIL.insert_image_link_into_list(
        RECORD_DICT[record_id],
        entry,
        image_name,
        KEY_FOR_FIRST_IMG)

if os.path.exists(FOLDER):
    # For each Record Page in folder, populate the front matter variable
    # IMAGES_FRONT_MATTER_VARIABLE_NAME with the url of the Googe Drive images.
    for file in os.listdir(FOLDER):
        yaml = YAML()
        file_name = os.fsdecode(file)
        record_page_path = FOLDER + file_name
        # Remove the first and last line from the file, this is because
        # those lines contains dashes that tells Jekyll that the lines
        # inbetween those two are front matter. We remove the dashes
        # so that we can process the front matter.
        UTIL.remove_first_and_last_line(record_page_path)
        # Open record page and write
        with open(record_page_path) as record_page:
            objyaml = yaml.load(record_page.read())
            record_id = objyaml[ID_FRONT_MATTER_VARIABLE_NAME]
            UTIL.create_empty_list_if_no_images_key(objyaml)
            if record_id in RECORD_DICT:
                for row in RECORD_DICT[record_id]:
                    item = {'image_path': row['URL'], 'title': row['Name']}
                    UTIL.insert_image_link_into_list(
                        objyaml['images'], item, item['title'], KEY_FOR_FIRST_IMG)
            UTIL.write_image_front_matter(objyaml, record_page_path, yaml)
print("FINISH")
