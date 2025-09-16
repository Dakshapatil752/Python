def write_file(filepath, content):
    """Write content to a file."""
    with open(filepath, 'w') as f:
        f.write(content)
