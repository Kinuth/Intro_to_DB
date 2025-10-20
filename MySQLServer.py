import mysql.connector
from mysql.connector import errorcode

def create_database():
    """Connects to a MySQL server and creates the alx_book_store database."""
    
    # --- IMPORTANT ---
    db_config = {
        'user': 'root',
        'password': '@1234',
        'host': 'localhost'
    }
    
    connection = None
    try:
        # Establish the connection to the MySQL server
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # SQL command to create the database if it doesn't exist
        # This avoids errors if the script is run multiple times.
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle specific connection errors or other MySQL errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Failed to create database: {err}")
    finally:
        # Ensure the connection is always closed
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
