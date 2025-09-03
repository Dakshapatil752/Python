#Check whether a path is a directory in Pyth

import os

path = 'new_directory'  # Change this to your path

if os.path.isdir(path):
    print(f"'{path}' is a directory.")
else:
    print(f"'{path}' is not a directory.")
