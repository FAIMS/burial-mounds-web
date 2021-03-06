#!/usr/bin/env python3
"""Module that makes the record pages."""

import csv
import os
import datetime
from ruamel.yaml import YAML

import util as UTIL
from category_generation import generate_category
from consts import ID_FRONT_MATTER_VARIABLE_NAME, IMAGES_FRONT_MATTER_VARIABLE_NAME, \
    RECORD_ID_COLUMN_NAME, CSV_FILE_NAME, TEMPLATE_FILE_NAME, GENERIC_RECORD_PAGE_TITLE


SHEET = CSV_FILE_NAME
TEMPLATE = TEMPLATE_FILE_NAME
DEST = '../_posts'

# The list that will be used to hold dictonaries where each dictionary
# correspond to a row in the CSV.
OBJECTS = []  # PLEASE DO NOT MODIFY.
# The list that will be used to hold the column names of the CSV.
CSV_HEADINGS = []  # PLEASE DO NOT MODIFY.

# A generic title for each Record Page which will be concatenated with the
# id of each Record.
TITLE = GENERIC_RECORD_PAGE_TITLE

# Creates a list of dictionary where each dict correspond to a row in the csv,
# each key correspond to the column names and store that into the list objects
# PLEASE DO NOT MODIFY THE NEXT 5 LINES OF CODE.
with open(SHEET, newline='') as csv_file:
    SHEET_READER = csv.DictReader(csv_file)
    CSV_HEADINGS = SHEET_READER.fieldnames
    for row in SHEET_READER:
        OBJECTS.append(row)

# Make the directory where the all the Record Pages will be created in.
os.makedirs(DEST, exist_ok=True)

print("Generating Record Pages")

# Loop through objects list, each item in objects is a record
# create a corresponding page for that record with its front matter variables.
for obj in OBJECTS:
    # record_id stores the id of the record, the strip() method removes leading or
    # trailing characters refer to
    # https://docs.python.org/3/library/stdtypes.html#str.strip for
    # more information.
    record_id = obj[RECORD_ID_COLUMN_NAME].strip()  # PLEASE DO NOT MODIFY.
    # Store the date at the time of running this module.
    today_date = datetime.date.today()  # PLEASE DO NOT MODIFY.

    # target is the path of where the file for the Record will be made
    # this is done by joining the destination with the file name.
    record_page_file_name = "{0}-{1}.md".format(today_date,
                                                'TRAP' + record_id)
    target = os.path.join(DEST,
                          record_page_file_name)  # PLEASE DO NOT MODIFY.
    yaml = YAML()  # PLEASE DO NOT MODIFY
    with open(TEMPLATE) as template_file:  # PLEASE DO NOT MODIFY.
        objyaml = yaml.load(template_file.read())
        if 'subheadline' in objyaml:
            # Change the assigned value of objyaml['subheadline']
            # to your needs,for example, changing
            # objyaml['subheadline'] = "Collection: TRAP Mounds"  to
            # objyaml['subheadline'] = "Collection: Another type of collection"
            # will change the subheadline front matter variables of a Record to
            # Collection: Another type of collection.
            objyaml['subheadline'] = 'Collection: TRAP Mounds'

        # Assign the id of the record into the id front matter variable.
        objyaml[ID_FRONT_MATTER_VARIABLE_NAME] = record_id

        if 'Tag' in obj:
            objyaml['tags'] = obj['Tags'].split(' | ')

        # START PROCESS OF ADDING CATEGORIES FOR A RECORD.
        # Creates a list to hold the categories for a record.
        categories = []

        generate_category(record_id, categories)

        objyaml['categories'] = categories
        # END PROCESS OF ADDING CATEGORIES FOR A RECORD.

        # Assign the current data into the front matter variable date.
        objyaml['date'] = today_date

        # Add key:value pairs to the front matter, where each key correspond to a column
        # and the value is the value of the column for that row.
        for heading in CSV_HEADINGS:
            heading_with_no_space = heading.replace(" ", "_").lower()
            # Exclude adding the key:value pair for the column that is the id
            # that is because, we have it in the front matter variable
            # record_id,
            if heading != RECORD_ID_COLUMN_NAME:
                objyaml[heading_with_no_space] = obj[heading]

        # Assign value to the front matter variable title,
        objyaml['title'] = TITLE + record_id

        # Remove the dummy values for images front matter, so that the Record
        # photo galley will display default image instead.
        objyaml[IMAGES_FRONT_MATTER_VARIABLE_NAME] = []
        UTIL.delete_images_key_from_yaml_dict_value_false(objyaml)
        # This will write the value of objyaml which contains the front matter variable
        # into the target file.
        UTIL.dump(target, yaml, objyaml)


print("FINISHED")
