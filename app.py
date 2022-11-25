#!/usr/bin/python3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute ('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('test_post.html', posts=posts)

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/createpost/')
def createpost():
    return render_template('createPost.html')

@app.route('/posts/')
def posts():
    return render_template('posts.html')

@app.route('/register/')
def register():
    return render_template('register.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('test_post'))

    return render_template('test_register.html')
app.run(debug=True)