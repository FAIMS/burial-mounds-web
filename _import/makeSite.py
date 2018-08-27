#!/usr/bin/env python3

import csv
import os
import sys
from pprint import pprint
import ruamel.yaml
from ruamel.yaml import YAML
import shutil
from pathlib import Path
import datetime
import re
import fnmatch
import glob

import dumpYaml as DUMP

SHEET = "MergeCSV.csv"
TEMPLATE = "template.yaml"
DEST = "../_posts"

# Name of the collection of the Records Pages
collectionname = "TRAP Mounds"

# The list that will be used to hold dictonaries where each dictionary
# correspond to a row in the csv
objects = []  # PLEASE DO NOT MODIFY
# The list that will be used to hold the column names of the csv
headers = []  # PLEASE DO NOT MODIFY

# Name of the column for the uuid
uuid = 'TRAP ID'


# A generic title for each Record Page which will be concatenated with the
# uuid of each Record
title = "TRAP Mound - "

# Creates a list of dictionary where each dict correspond to a row in the csv, each key correspond to the column names and store that
# into the list objects
# PLEASE DO NOT MODIFY THE NEXT 5 LINES OF CODE
with open(SHEET, newline='') as csvfile:
    sheetreader = csv.DictReader(csvfile)
    headers = sheetreader.fieldnames
    for row in sheetreader:
        objects.append(row)

# Make the directory where the all the Record Pages will be created in
os.makedirs('../_posts/', exist_ok=True)

print("Generating Record Pages")

# Loop through objects list, each item in objects is a record
# create a corresponding page for that record with its front matter variables
for obj in objects:
    # id stores the uuid of the record, the strip() method removes leading or trailing characters
    # refer to https://docs.python.org/3/library/stdtypes.html#str.strip for
    # more information
    id = obj[uuid].strip()  # PLEASE DO NOT MODIFY

    # target is the path of where the file for the Record will be made
    # this is done by joining the destination with the filename
    target = os.path.join(DEST,
                          "{0}-{1}.md".format(datetime.date.today(),
                                              'TRAP' + id))  # PLEASE DO NOT MODIFY
    yaml = YAML()  # PLEASE DO NOT MODIFY
    with open(TEMPLATE) as templatefile:  # PLEASE DO NOT
        objyaml = yaml.load(templatefile.read())
        if 'subheadline' in objyaml:
            # Change the assigned value of objyaml['subheadline'] to your needs, for example, changing
            # objyaml['subheadline'] = "Collection: TRAP Mounds"  to
            # objyaml['subheadline'] = "Collection: Another type of collection"
            # will change the subheadline front matter variables of a Record to
            # Collection: Another type of collection
            objyaml['subheadline'] = "Collection: TRAP Mounds"

        # Assign the id of the record into the uuid front matter variable
        objyaml['uuid'] = id

        if 'Tag' in obj:
            objyaml['tags'] = obj['Tags'].split(' | ')

        # START PROCESS OF ADDING CATEGORIES FOR A RECORD
        # Creates a list to hold the categories for a record
        categories = []
        # Change the following if and else if statements according to your
        # needs
        if int(id) in range(1000, 2000):
            categories.append("1000-1999")
        elif int(id) in range(2000, 3000):
            categories.append("2000-2999")
        elif int(id) in range(3000, 4000):
            categories.append("3000-3999")
        elif int(id) in range(4000, 5000):
            categories.append("4000-4999")
        elif int(id) in range(5000, 6000):
            categories.append("5000-5999")

        objyaml['categories'] = categories
        # END PROCESS OF ADDING CATEGORIES FOR A RECORD

        # Assign the current data into the front matter variable date
        objyaml['date'] = datetime.date.today()

        # Add key:value pairs to the front matter, where each key correspond to a column
        # and the value is the value of the column for that row
        for k in headers:
            k_with_no_space = k.replace(" ", "_").lower()
            # Exclude adding the key:value pair for the column that is the uuid
            # that is because, we have it in the front matter variable uuid
            if k != uuid:
                objyaml[k_with_no_space] = obj[k]

        # Assign value to the front matter variable title
        objyaml['title'] = title + id

        # If there are no images then remove the images front matter for that Record
        # so that the Record photo gallery will display default image instead
        objyaml['images'] = []
        if len(objyaml['images']) == 0:
            objyaml.pop('images', None)

        # This will write the value of objyaml which contains the front matter variable
        # into the target file
        DUMP.dump(target, yaml, objyaml)


print("FINISHED")
