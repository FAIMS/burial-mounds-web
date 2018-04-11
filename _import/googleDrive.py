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

SHEET = "BM-Pic.csv"
DEST = "../_posts"

# Name of the collection of the Records Pages
# TODO: If th
collectionname = "TRAP Mounds"

objects = []
headers = []
d = {}
with open(SHEET, newline='') as csvfile:
    sheetreader = csv.DictReader(csvfile)
    headers = sheetreader.fieldnames
    for row in sheetreader:
        objects.append(row)


# Name of the column for the uuid
uuid = 'TRAP ID'
keyforfirstimg = 'overview'
keylen = 4
folder = "../_posts/"

remove = "https://drive.google.com/file/d/"

prepend_link = "https://drive.google.com/uc?id="

print("append")
for row in objects:
    name = row['Name']
    # Get the uuid that correspond for that image
    id = name[:keylen]
    # Preprocessing
    s = row['URL'].replace(remove,"")
    s = s.replace("/view?usp=drivesdk", "")
    # If first image then create a empty list first
    if id not in d:
        d[id] = []
    # url
    s = prepend_link + s
    entry = {'Name': name, 'URL': s}
    if 'Overview' in name:
        d[id].insert(0,entry)
    else:
        d[id].append(entry)

if os.path.exists(folder):
    # For each Record Page in folder
    for file in os.listdir(folder):
        yaml = YAML()
        filename = os.fsdecode(file)
        recordpagepath = folder+filename
        lines = open(recordpagepath).readlines()
        open(recordpagepath, 'w').writelines(lines[1:-1])
        with open(recordpagepath) as recordpage:
            objyaml=yaml.load(recordpage.read())
            recordid = objyaml[uuid.replace(" ", "_").lower()]
            if 'images' not in objyaml:
                objyaml['images'] = []
            if recordid in d:
                for row in d[recordid]:
                    #print(row)
                    objyaml['images'].append({'image_path': row['URL'], 'title': row['Name']})

            if len(objyaml['images']) == 0:
                objyaml.pop('images', None)
            DUMP.dump(recordpagepath,yaml,objyaml)
print("finish")
