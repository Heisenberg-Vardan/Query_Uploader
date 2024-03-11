import yaml

def get_database_config(file_path):
    """
    Parses database configuration values from a YAML file.

    Args:
        file_path (str): The path to the YAML file containing database configuration.

    Returns:
        dict: A dictionary containing database configuration values.
    """
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
            return config
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
        return None

