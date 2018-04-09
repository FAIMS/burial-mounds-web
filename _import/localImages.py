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
            default_img_path = "/images/"  + recordid
            if os.path.exists(".."+ default_img_path):
                print("exist")
                for file in os.listdir(".."+default_img_path):
                    filename = os.fsdecode(file)
                    print(default_img_path + filename)
                    objyaml['images'].append({'image_path': default_img_path +'/'+ filename, 'title': filename})
            if len(objyaml['images']) == 0:
                objyaml.pop('images', None)
            DUMP.dump(recordpagepath,yaml,objyaml)
print("finish")
