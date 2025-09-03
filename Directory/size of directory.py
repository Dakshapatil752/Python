"""
Get the size of a directory in Python
"""

import os

def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            if os.path.isfile(filepath):
                total_size += os.path.getsize(filepath)
    return total_size

# Change 'new_directory' to your target directory
directory = 'new_directory'
size_bytes = get_directory_size(directory)
print(f"Size of directory '{directory}': {size_bytes} bytes")
