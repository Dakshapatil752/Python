def read_file(filepath):
    """Read and return the contents of a file."""
    with open(filepath, 'r') as f:
        return f.read()
