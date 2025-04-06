import mysql.connector  # lets Python talk to your MySQL database server.

       
def connect_db():              # defines a function to create a connection of database and return
    conn = mysql.connector.connect(        
        host="localhost",       # replace with your host name
        user="root",         
        password="root123",     # replace with your real password
        database="expense_db"   # replace with your database name
    )
    cursor = conn.cursor()      #Creates a cursor object from the connection.


    return conn, cursor         # Returns connection and cursor

