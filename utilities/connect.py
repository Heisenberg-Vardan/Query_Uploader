import mysql.connector
from utilities.get_config import get_database_config


def get_connector(path):
    """
    Establishes a connection to a MySQL database using the configuration provided in a YAML file.

    Args:
        path (str): The path to the YAML file containing database configuration.

    Returns:
        MySQLConnection or None: A connection object to the MySQL database if successful, otherwise None.
    """
    database_config = get_database_config(path)
    if database_config is None:
        return None
    
    try:
        cnx = mysql.connector.connect(user=database_config.get('USERNAME'), 
                                      password=database_config.get('PASSWORD'),
                                      host=database_config.get('SERVER'), 
                                      database=database_config.get('DATABASE'),
                                      auth_plugin='mysql_native_password')
        return cnx
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
