# Get the modification time of a directory in Python

import os
import time

directory = 'new_directory'  # Change to your target directory

if os.path.exists(directory) and os.path.isdir(directory):
    mod_time = os.path.getmtime(directory)
    readable_time = time.ctime(mod_time)
    print(f"Modification time of directory '{directory}': {readable_time}")
else:
    print(f"Directory '{directory}' does not exist.")

"""
Create a directory in Python
"""

import os

directory = 'new_directory'  # Change to your desired directory name

try:
    os.mkdir(directory)
    print(f"Directory '{directory}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory}' already exists.")
