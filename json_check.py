# A program to check the validity of a JSON file

import json
import sys
import os

# user inputs file on prompt?



if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("The JSON file is VALID!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: json_check.py <file_path/file_name>")