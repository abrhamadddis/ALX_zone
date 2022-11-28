#!/usr/bin/python3
import sqlite3

connection = sqlite3.connect('test.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO user (name, email, password) VALUES (?, ?, ?)",
            ('alx', 'alxzone@gmail.com', 'alxzonego')
            )

connection.commit()
connection.close()