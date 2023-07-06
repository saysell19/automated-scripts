# A program to convert JSON to YAML

import json
import yaml
import sys
import os


if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json_data = json.load(file)
        file.close()
        yaml_data = yaml.dump(json_data)
        print(yaml_data)
    else:
        print(sys.argv[1] + " not found")