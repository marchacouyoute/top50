import mysql.connector
from mysql.connector.errors import Error


def create_connection(path):
    connection = None
    try:
        connection = mysql.connect(path)
        print('Connection to DB is successful')
    except Error as e:
        print(f"The error '{e}' occured")
    return connection


connection = create_connection("C:\\top50.mysql")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occured")
