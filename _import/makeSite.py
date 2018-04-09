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

parser = argparse.ArgumentParser(description='')
parser.add_argument('-s', '--sheet', help='Complete file path + name of csv file')
parser.add_argument('-t', '--template', help='Complete file path + name of template yaml file for Records')
parser.add_argument('-u', '--uuid', help='Column name of the uuid')
parser.add_argument('-r', '--recordtitle', help='Generic title for each record page which will be prepend')
#parser.add_argument('-h', '--subheadline', help='subheadline for record')
#parser.add_argument('-c', '--collection', help='Name of the collection')

# TODO: Assume Subheadline and collection is one of the coolumns

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
        #print(templatefile.read())
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
        default_img_path = "/images/"  + str(id)
        if os.path.exists(".."+default_img_path):
            for file in os.listdir(".."+default_img_path):
                filename = os.fsdecode(file)
                objyaml['images'].append({'image_path': default_img_path + "/" + filename, 'title': filename})

        if len(objyaml['images']) == 0:
            objyaml.pop('images', None)
        #objyaml['trap_id'] = id
        def startendlines(s):
            return "---\n{0}---\n".format(s)
        with open(target, 'w') as targetyamlfile:
        	yaml.dump(objyaml, targetyamlfile, transform=startendlines)
