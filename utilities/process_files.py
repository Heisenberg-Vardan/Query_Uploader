import mysql.connector
import re

def process_data(query_name, version, sql_query, table_name, existing_queries, data, connector):
    """
    Process data to check if a query already exists in the database table and updates it if necessary.

    Args:
        query_name (str): The name of the query.
        version (str): The version of the query.
        sql_query (str): The SQL query content.
        table_name (str): The name of the database table.
        existing_queries (set): A set containing existing query names.
        data (list): List of tuples containing existing query data from the database.
        connector (MySQLConnection): A connection object to the MySQL database.
    """
    if query_name not in existing_queries and len(existing_queries) == 0:
        insert_sql_content(query_name, version, sql_query, table_name, connector)
        print(f'New query {query_name}, version {version} added successfully')
    else:
        for row in data:
            if query_name == row[0] and version == row[1]:
                if sql_query == row[2]:
                    print(f'Query: {query_name}, Version {version} already exists')
                    break
                elif sql_query != row[2]:
                    delete_sql_content(query_name, version, table_name, connector)
                    insert_sql_content(query_name, version, sql_query, table_name, connector)
                    print(f'Current version for {query_name} updated successfully')
                    break
            elif query_name == row[0] and version != row[1]:
                if sql_query != row[2]:
                    if check_sql_content(table_name, query_name, version, sql_query, connector):
                        print(f'Query: {query_name}, Version {version} already exists')
                        break

def check_sql_content(table_name, query_name, version, sql_query, connector):
    """
    Check if the given query already exists in the database table.

    Args:
        table_name (str): The name of the database table.
        query_name (str): The name of the query.
        version (str): The version of the query.
        sql_query (str): The SQL query content.
        connector (MySQLConnection): A connection object to the MySQL database.

    Returns:
        list: List of tuples containing existing query data if found, else None.
    """
    try:
        cursor = connector.cursor()

        sql = f"SELECT * FROM {table_name} WHERE query_name = %s AND version = %s AND sql_query = %s"
        sql_query = re.sub('"', '""', sql_query)
        cursor.execute(sql, (query_name, version, sql_query))
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def get_sql_content(table_name, connector):
    """
    Retrieve all data from the database table.

    Args:
        table_name (str): The name of the database table.
        connector (MySQLConnection): A connection object to the MySQL database.

    Returns:
        list: List of tuples containing data from the database table if successful, else None.
    """
    try:
        cursor = connector.cursor()

        sql = f"SELECT * FROM {table_name} ORDER BY query_name"
        
        cursor.execute(sql)
        return cursor.fetchall()
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def insert_sql_content(query_name, version, sql_query, table_name, connector):
    """
    Insert a new query into the database table.

    Args:
        query_name (str): The name of the query.
        version (str): The version of the query.
        sql_query (str): The SQL query content.
        table_name (str): The name of the database table.
        connector (MySQLConnection): A connection object to the MySQL database.
    """
    try:
        cursor = connector.cursor()

        sql = f"INSERT INTO {table_name} (query_name, version, sql_query) VALUES (%s, %s, %s)"

        sql_query = re.sub('"', '""', sql_query)

        cursor.execute(sql, (query_name, version, sql_query))

        connector.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_sql_content(query_name, version, table_name, connector):
    """
    Delete an existing query from the database table.

    Args:
        query_name (str): The name of the query.
        version (str): The version of the query.
        table_name (str): The name of the database table.
        connector (MySQLConnection): A connection object to the MySQL database.
    """
    try:
        cursor = connector.cursor()

        sql = f"DELETE FROM {table_name} WHERE query_name = %s AND version = %s"

        cursor.execute(sql, (query_name, version))

        connector.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")