import os

def read_directory(directory_path):
    """
    Reads a directory and returns the name, version, and content of each file.

    Args:
        directory_path (str): The path to the directory.

    Returns:
        list of dict: A list of dictionaries containing name, version, and content of each file.
    """
    file_data = []

    for filename in os.listdir(directory_path):
        filepath = os.path.join(directory_path, filename)
        if os.path.isfile(filepath):
            name, version = filename.rsplit('_', 1)
            version = version.rsplit('.', 1)[0]
            
            with open(filepath, 'r') as file:
                content = file.read()

            file_info = {
                'name': name,
                'version': version,
                'content': content
            }
            file_data.append(file_info)

    return file_data