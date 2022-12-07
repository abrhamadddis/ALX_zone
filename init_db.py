#!/usr/bin/python3
import sqlite3
from datetime import datetime

connection = sqlite3.connect('test.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d')

# cur.execute("INSERT INTO user (name, email, password) VALUES (?, ?, ?)",
#             ('alx', 'alxzone@gmail.com', 'alxzonego')
#             )
# cur.execute("INSERT INTO posts (title, content, created, post_user_id) VALUES (?, ?, ?, ?)",
#             ('First Post', 'Content for the first post',formatted_date, 1)
#             )

# cur.execute("INSERT INTO posts (title, content, created, post_user_id) VALUES (?, ?, ?, ?)",
#             ('Second Post', 'Content for the second post',formatted_date, 1)
#             )
connection.commit()
connection.close()