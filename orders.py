from dbcon import conn, cursor, pyodbc
from lists import options
import random
import datetime
import time

loop = True

while loop:
    try:
        time.sleep(random.uniform(0.5,1))
        order = (( 
        random.randint(0,999), 
        options["items"][random.randint(0,len(options["items"])-1)], 
        options["grip_colors"][random.randint(0,len(options["grip_colors"])-1)], 
        options["sizes"][random.randint(0,len(options["sizes"])-1)], 
        'new', 
        datetime.datetime.now()))

        cursor.execute('INSERT INTO orders(customerID, item, gripColor, size, status, createdAt) VALUES (?,?,?,?,?,?)', order)
        conn.commit()
        print('Data Inserted')

    except pyodbc.Error as e:
        print("Error with query.", e)

