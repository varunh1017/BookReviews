import sqlite3

# establishing database connection and initializing cursor object 
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# executing the query for selecting all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# printing all table names
for table_name in tables:
    print(table_name[0])

# closing the connection
conn.close()