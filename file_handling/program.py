import sys
import os

# Always add the main Python directory to sys.path
main_python_dir = r'c:\Users\HP\Documents\files\Python'
if main_python_dir not in sys.path:
    sys.path.insert(0, main_python_dir)

from file_handling.file_read import read_file

from file_handling.file_read import read_file
from file_handling.file_write import write_file

# File paths (using the new data directory)
data_dir = r'c:\Users\HP\Documents\files\Python\file_handling\data'
file1 = os.path.join(data_dir, 'file1.txt')
file2 = os.path.join(data_dir, 'file2.txt')
file3 = os.path.join(data_dir, 'file3.txt')
file4 = os.path.join(data_dir, 'file4.txt')

def safe_read(filepath):
    try:
        return read_file(filepath)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return ''


# Read content from first two files
content1 = safe_read(file1)
content2 = safe_read(file2)
print("Content of file1:", content1)
print("Content of file2:", content2)

# Write combined content to third file
combined_content = content1 + content2
write_file(file3, combined_content)
print("Combined content written to file3.")

# Read content from fourth file
content4 = safe_read(file4)
print("Content of file4:", content4)

# Read the current content of file3
current_content = safe_read(file3)
print("Current content of file3 before appending:", current_content)

# Write the current content of file3 plus first 10 characters of file4 into file3
write_file(file3, current_content + content4[:10])
print("First 10 characters of file4 appended to file3.")