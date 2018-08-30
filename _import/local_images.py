#!/usr/bin/env python3
"""This module extract the path of images for a record for images stored locally
relative to the project inside the images folder"""
import os
from ruamel.yaml import YAML

import util as UTIL
from consts import FOLDER, ID_FRONT_MATTER_VARIABLE_NAME, KEY_FOR_FIRST_IMG

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
            default_img_path = "/images/" + record_id
            if os.path.exists(".." + default_img_path):
                for image in os.listdir(".." + default_img_path):
                    file_name = os.fsdecode(image)
                    image_path = default_img_path + '/' + file_name
                    item = {'image_path': image_path, 'title': file_name}
                    UTIL.insert_image_link_into_list(
                        objyaml['images'], item, file_name, KEY_FOR_FIRST_IMG)
            if not objyaml['images']:
                objyaml.pop('images', None)
            UTIL.dump(record_page_path, yaml, objyaml)
print("FINISH")
