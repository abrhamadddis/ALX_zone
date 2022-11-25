#!/usr/bin/python3
import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Mac tools for absolute beginners', 'Without further ado, here are 7mac tools I use on all my macs. Whenever I get a new mac, I set up these seven tools so I can start working in a more comfortable atmosphere, and they help me to increase my productivity.')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Implementing A Second Brain in Emacs and Org-Mode', 'This post is a continuation of “Building A Second Brain with Emacs and Org-Mode.” If you haven’t read that yet, read that post first. It gave a high level overview of how BASB extends GTD, what Emacs and Org-Mode')

            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Mac tools for absolute beginners', 'Without further ado, here are 7mac tools I use on all my macs. Whenever I get a new mac, I set up these seven tools so I can start working in a more comfortable atmosphere, and they help me to increase my productivity.')
            )
cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Mac tools for absolute beginners', 'Without further ado, here are 7mac tools I use on all my macs. Whenever I get a new mac, I set up these seven tools so I can start working in a more comfortable atmosphere, and they help me to increase my productivity.')
            )

connection.commit()
connection.close()