# Writing to a file

with open('seek_example.txt', 'w') as f:
    f.write('First line\nSecond line\nThird line')

# Reading from a file and using seek()
with open('seek_example.txt', 'r') as f:
    print("Reading first 5 characters:")
    
    print(f.read(5))  # Read first 5 characters
    f.seek(0)         # Move file pointer to the beginning
    
    print("\nReading the whole file after seek(0):")
    print(f.read())   # Read the whole file from the beginning
