import mysql.connector

# Connect to the database
try:
    import time 
    time.sleep(3)
    connection = mysql.connector.connect(
        host="mysql.railway.internal",
        user="root",
        password="fEg4bBahd4BDf23-gbagE3-eAbDFBda6",
        database="railway"
    )

    if connection.is_connected():
        print("Connected to MySQL database")

    # Perform database operations here

except mysql.connector.Error as e:
    print("Error connecting to MySQL database:", e)

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed")
