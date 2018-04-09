import sys
import ruamel.yaml
from ruamel.yaml import YAML

def dump(filepath,yaml,objyaml):
    def startendlines(s):
        return "---\n{0}---\n".format(s)
    with open(filepath, 'w') as targetyamlfile:
        yaml.dump(objyaml, targetyamlfile, transform=startendlines)
