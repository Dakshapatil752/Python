import os
import shutil

dir_name = 'new_directory'
if os.path.exists(dir_name):
    shutil.rmtree(dir_name)
    print(f"Directory '{dir_name}' removed.")
else:
    print(f"Directory '{dir_name}' does not exist.")

# remove a file
file_name = 'sample.txt'
if os.path.exists(file_name):
    os.remove(file_name)
    print(f"File '{file_name}' removed.")
else:
    print(f"File '{file_name}' does not exist.")