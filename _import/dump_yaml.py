"""Module that contain a function to output the yaml into a file"""


def dump(filepath, yaml, objyaml):
    """Write the value of objyaml into filepath"""
    def startendlines(input_str):
        """Return formatted string"""
        return "---\n{0}---\n".format(input_str)
    with open(filepath, 'w') as targetyamlfile:
        yaml.dump(objyaml, targetyamlfile, transform=startendlines)
