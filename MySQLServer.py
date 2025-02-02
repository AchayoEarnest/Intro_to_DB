import mysql.connector

try:
    # Connect to MySQL Server
    conn = mysql.connector.connect(
        host="localhost",
        user="earnest",
        password="access2023"
    )
    cursor = conn.cursor()
    
    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close connections
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
