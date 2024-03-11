from utilities.connect import get_connector
from utilities.read_files import read_directory
from utilities.get_config import get_database_config
from utilities.process_files import process_data
from utilities.process_files import get_sql_content

config_file_path = r'C:\Users\varda\Desktop\PON_Demo\config\config.yml'
directory_path = r'C:\Users\varda\Desktop\PON_Demo\test_data'


cnx = get_connector(config_file_path)

if cnx:
    print("Connection to the database established successfully!")
else:
    print("Failed to establish connection to the database.")


queryset = read_directory(directory_path)

table_name = get_database_config(config_file_path).get('TABLE')

data = get_sql_content(table_name, cnx)
table_queries =[]
for query in data:
    if query[0] not in table_queries:
        table_queries.append(query[0])

for queries in queryset:
    process_data(queries['name'], queries['version'], queries['content'], table_name, table_queries, data,  cnx)
