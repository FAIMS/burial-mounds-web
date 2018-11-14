"""Module that defined shared constants used by the other modules in the _import folder.
Read from the customizable-variables.yaml file and"""
from ruamel.yaml import YAML

# File name of the yaml file that contains the customizable variables.
CUSTOMIZABLE_VARIABLES_YAML_FILE_NAME = "customizable-variables.yaml"
# List that will contain the variables
CUSTOM_VARIABLES = []
# Read all the variables from the file and store it into CUSTOM_VARIABLES.
with open(CUSTOMIZABLE_VARIABLES_YAML_FILE_NAME) as file:
    YAML = YAML(typ='safe')
    CUSTOM_VARIABLES = YAML.load(file)

print(CUSTOM_VARIABLES)

# Name of the collection of the Records Pages
COLLECTION_NAME = CUSTOM_VARIABLES['collection_name']
# Name of the front matter variable for the record id
ID_FRONT_MATTER_VARIABLE_NAME = 'record_id'
# Name of the front matter variable for the image_list
IMAGES_FRONT_MATTER_VARIABLE_NAME = 'images'
# Keyword that identify the first image for a record
KEY_FOR_FIRST_IMG = CUSTOM_VARIABLES['key_for_first_img']
# Length of the uuid
KEY_LEN = CUSTOM_VARIABLES['key_len']
# Path to the folder that contains the record file
FOLDER = "../_posts/"
# Name of the column for the record id
RECORD_ID_COLUMN_NAME = CUSTOM_VARIABLES['record_id_column_name']
# File name of the CSV with the record data.
CSV_FILE_NAME = CUSTOM_VARIABLES['csv_file_name']
# File name of the template.
TEMPLATE_FILE_NAME = CUSTOM_VARIABLES['template_file_name']
# A generic title for each Record Page which will be concatenated with the
# id of each Record
GENERIC_RECORD_PAGE_TITLE = CUSTOM_VARIABLES['generic_record_page_title']
