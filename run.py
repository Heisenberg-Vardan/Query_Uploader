import sys
from utilities.connect import get_connector
from utilities.read_files import read_directory
from utilities.get_config import get_database_config
from utilities.process_files import process_data
from utilities.process_files import get_sql_content

def main(config_file_path, directory_path):
    """
    Main function to process query files and update the database accordingly.

    Args:
        config_file_path (str): The path to the configuration file.
        directory_path (str): The path to the directory containing query files.
    """
    # Establish database connection
    connector = get_connector(config_file_path)

    # Check if connection is successful
    if connector:
        print("Connection to the database established successfully!")
    else:
        print("Failed to establish connection to the database.")
        return

    # Read directory to get query files
    queryset = read_directory(directory_path)

    # Get database table name from config
    table_name = get_database_config(config_file_path).get('TABLE')

    # Get existing queries from the database
    data = get_sql_content(table_name, connector)
    table_queries = set(row[0] for row in data)

    # Process each query file
    for query_info in queryset:
        process_data(query_info['name'], query_info['version'], query_info['content'],
                      table_name, table_queries, data, connector)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <config_file_path> <directory_path>")
    else:
        config_file_path = sys.argv[1]
        directory_path = sys.argv[2]
        main(config_file_path, directory_path)
