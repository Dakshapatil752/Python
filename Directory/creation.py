"""
Create a new directory and write data to a file in Python
"""

import os

directory = 'new_directory'  # Change to your desired directory name
filename = 'data.txt'
filepath = os.path.join(directory, filename)

try:
    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    print(f"Directory '{directory}' created or already exists.")

    # Write data to a file in the new directory
    with open(filepath, 'w') as f:
        f.write('This is some sample data written to a file in the new directory.')
    print(f"Data written to {filepath}")

except Exception as e:
    print(f"Error: {e}")
