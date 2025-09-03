
#Check whether a directory exists in Python

import os

dir_name = 'new_directory'

if os.path.exists(dir_name) and os.path.isdir(dir_name):
    print(f"Directory '{dir_name}' exists.")
else:
    print(f"Directory '{dir_name}' does not exist.")