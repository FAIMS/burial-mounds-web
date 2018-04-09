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
SHEET = "09_03-Mounds_short.csv"
TEMPLATE = "template.yaml"
DEST = "../_posts"

# Name of the collection of the Records Pages
# TODO: If th
collectionname = "TRAP Mounds"

objects = []
headers = []

# Name of the column for the uuid
uuid = 'TRAP ID'


# A generic title for each Record Page which will be concat with the uuid of each Record
title = "TRAP Mound - "

# Creates a list of dictionary where each dict correspond to a row in the csv, each key correspond to the column names
with open(SHEET, newline='') as csvfile:
    sheetreader = csv.DictReader(csvfile)
    headers = sheetreader.fieldnames
    for row in sheetreader:
        objects.append(row)

# Make the directory where the all the Record Pages will be created in

os.makedirs('../_posts/', exist_ok=True)

#if uuid in headers:
#    headers.remove(uuid)

for obj in objects:
    id = obj[uuid].strip()
    target = os.path.join(DEST, "{0}-{1}.md".format(datetime.date.today(), 'TRAP'+id))
    yaml = YAML()
    with open(TEMPLATE) as templatefile:
        objyaml=yaml.load(templatefile.read())
        if 'subheadline' in objyaml:
            objyaml['subheadline'] = "Collection: TRAP Mounds"
        if 'Tag' in obj:
            objyaml['tags'] = obj['Tags'].split(' | ')
        objyaml['categories'] = [collectionname]
        objyaml['date'] = datetime.date.today()
        for k in headers:
            k_with_no_space = k.replace(" ", "_").lower()
            objyaml[k_with_no_space] = obj[k]
        objyaml['title'] =  title + id

        objyaml['images'] = []
        if len(objyaml['images']) == 0:
            objyaml.pop('images', None)
        #objyaml['trap_id'] = id
        DUMP.dump(target,yaml,objyaml)
