"""Module that contains helper functions used by other modules in this project."""

from consts import IMAGES_FRONT_MATTER_VARIABLE_NAME

def dump(file_path, yaml, objyaml):
    """Write the value of objyaml into file path."""
    def start_end_lines(input_str):
        """Return formatted string"""
        return "---\n{0}---\n".format(input_str)
    with open(file_path, 'w') as target_yaml_file:
        yaml.dump(objyaml, target_yaml_file, transform=start_end_lines)


def insert_image_link_into_list(image_list, item, image_title, keyword):
    """Insert item into the list."""
    if keyword.lower() in image_title.lower():
        image_list.insert(0, item)
    else:
        image_list.append(item)


def remove_first_and_last_line(file_path):
    """Remove the first and last line of a file."""
    page_lines = open(file_path).readlines()
    open(file_path, 'w').writelines(page_lines[1:-1])


def delete_key_from_dict_if_value_falsy(dictionary, key):
    """Remove key from dictionary if the value is falsy."""
    if not dictionary[key]:
        dictionary.pop(key, None)

def delete_images_key_from_yaml_dict_value_false(yaml_list):
    delete_key_from_dict_if_value_falsy(yaml_list,
        IMAGES_FRONT_MATTER_VARIABLE_NAME)

def write_image_front_matter(yaml_list, page_path,
                                yaml, remove_if_empty=True):
    """Write the yaml_list into Record Page, remove the
image_front_matter key if value for that key is falsy"""
    if remove_if_empty:
        # If 'images' list is empty then remove it from objyaml.
        delete_images_key_from_yaml_dict_value_false(yaml_list)
    # Write to record page.
    dump(page_path, yaml, yaml_list)

def create_empty_list_if_no_key(d, key):
        if key not in d:
            d[key] = []

def create_empty_list_if_no_images_key(d):
    """If there is no front matter variable called 'images'
then create it and make it a empty list."""
    create_empty_list_if_no_key(d, IMAGES_FRONT_MATTER_VARIABLE_NAME)
