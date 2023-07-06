# A program to check the validity of a YAML file

import yaml
import sys
import os


if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load(file.read())
        file.close()
        print("The YAML file is VALID!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: yaml_check.py <file_path/file_name>")