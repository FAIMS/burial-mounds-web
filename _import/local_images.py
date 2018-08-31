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
        # Relative path to record page
        record_page_path = FOLDER + file_name
        UTIL.remove_first_and_last_line(record_page_path)
        # Open record page and write
        with open(record_page_path) as record_page:
            objyaml = yaml.load(record_page.read())
            record_id = objyaml[ID_FRONT_MATTER_VARIABLE_NAME]
            # If there is no front matter variable called 'images'
            # then create it and make it a empty list
            if 'images' not in objyaml:
                objyaml['images'] = []
            default_img_path = "/images/" + record_id
            if os.path.exists(".." + default_img_path):
                # Insert key value pair into 'images' list
                for image in os.listdir(".." + default_img_path):
                    file_name = os.fsdecode(image)
                    image_path = default_img_path + '/' + file_name
                    item = {'image_path': image_path, 'title': file_name}
                    UTIL.insert_image_link_into_list(
                        objyaml['images'], item, file_name, KEY_FOR_FIRST_IMG)
            UTIL.delete_key_from_dict_if_value_falsy(
                objyaml, IMAGES_FRONT_MATTER_VARIABLE_NAME)
            UTIL.dump(record_page_path, yaml, objyaml)
print("FINISH")
