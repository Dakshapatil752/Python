def upload_file(source, destination):
    """Upload (copy) a file from source to destination."""
    import shutil
    shutil.copy(source, destination)
