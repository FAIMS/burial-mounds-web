# _import README <!-- omit in toc -->

In this folder are files used to generate ```record pages```.

## Table of Contents <!-- omit in toc -->

- [make_site.py](#makesitepy)
- [google_drive.py](#googledrivepy)
- [local_images.py](#localimagespy)
- [consts.py](#constspy)
- [category_generation.py](#categorygenerationpy)
- [csv_merge.py](#csvmergepy)
- [customizable-variables.yml](#customizable-variablesyml)

## make_site.py

This script is used to generate `record pages` from the given CSV.

## google_drive.py

The script is used to used to write the URL to images hosted on Google Drive for a associated record page. User will need to ensure that the CSV is in the *_import* folder, and that the name of CSV matches the value of the key `google_drive_csv_file` in the customizable-variables.yaml file.

## local_images.py

This script is used to write the paths to images for a associated record page.

## consts.py

This Python file contains constants that will be used by the other scripts.

## category_generation.py

This script is used to generate the category for `record pages`. The `generate_category` method append to the `categories` list based on the value of the `record_id`, modify the if condition inside the method to your requirements.

## csv_merge.py

A python script written in Python3 that can be used to merge two CSV file based on a key.

[Back to TOC](#table-of-contents)

## customizable-variables.yml

This YAML file contains variables that will be used by the above scripts. To customize the generated `record pages`, please adjust the variables to your needs.