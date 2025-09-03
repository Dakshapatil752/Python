# Writing to a file
with open('example.txt', 'w') as f:
    f.write('Hello, this is a sample text file.\n')
    f.write('This is the second line.')
print("Data written to example.txt")

# Reading from a file
with open('example.txt', 'r') as f:
    content = f.read()
    print("Content of example.txt:")
    print(content)
