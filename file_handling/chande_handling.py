def handle_change(filepath, new_content):
    """Change the content of a file safely."""
    try:
        with open(filepath, 'w') as f:
            f.write(new_content)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
