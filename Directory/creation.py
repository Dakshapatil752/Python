"""
Create a new directory in Python (works for nested directories)
"""

import os

directory = 'new_directory'  # Change to your desired directory name

try:
    os.makedirs(directory, exist_ok=True)
    print(f"Directory '{directory}' created or already exists.")
except Exception as e:
    print(f"Error creating directory: {e}")
