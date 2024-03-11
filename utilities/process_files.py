import mysql.connector
import re


def process_data(name, version, sql_content, table_name, table_queries, data, connector):
    if name not in table_queries:
        insert_sql_content(name, version, sql_content, table_name, connector)
        print(f'New query {name} added successfully')
    else:
        for row in data:
            if name == row[0] and version == row[1] and sql_content == row[2]:
                print(f'Query: {name} already exists')
                break
            elif name == row[0] and version == row[1] and sql_content != row[2]:
                delete_sql_content(name, version, table_name, connector)
                insert_sql_content(name, version, sql_content, table_name, connector)
                print(f'Current version for {name} updated successfully')
                break
            elif name == row[0] and version != row[1] and sql_content != row[2]:
                insert_sql_content(name, version, sql_content, table_name, connector)
                print(f'New version for {name} added successfully')
                break

        



def get_sql_content(table_name, connector):
    try:
        cursor = connector.cursor()

        sql = f"SELECT * from {table_name} ORDER BY query_name"
        
        cursor.execute(sql)
        return cursor.fetchall()
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
    
def insert_sql_content(name, version, sql_content, table_name, connector):
    try:
        cursor = connector.cursor()

        sql = f"INSERT INTO {table_name} (query_name, version, sql_query) VALUES (%s, %s, %s)"

        sql_content = re.sub('"', '""', sql_content)

        cursor.execute(sql, (name, version, sql_content))

        connector.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def delete_sql_content(name, version, table_name, connector):
    try:
        cursor = connector.cursor()

        sql = f"DELETE FROM {table_name} WHERE query_name = %s AND version = %s"

        cursor.execute(sql, (name, version))

        connector.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
