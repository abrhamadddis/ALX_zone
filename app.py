#!/usr/bin/python3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd6bb525dd12c9953922f61784e785ba147f643b5d515ba0f'
def get_db_connection():
    conn = sqlite3.connect('alx.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/register/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed=generate_password_hash(password, method='sha256')
        pwd = request.form['pwd']

        if not name:
            flash('name is required')
        elif not email:
            flash('email is required')
        elif not password:
            flash('password is required')
        elif not pwd:
            flash('confirmatin password is required')
        elif password != pwd:
            flash('password did not match')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO user (name, email, password) VALUES (?, ?, ?)',
                         (name, email, hashed))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/createpost/', methods=('GET', 'POST'))
def createpost():
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
            return redirect(url_for('post'))
    return render_template('createPost.html')

app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?', (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('post'))

    return render_template('edit.html', post=post)

@app.route('/posts/')
def post():
    conn=get_db_connection()
    posts=conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('posts.html', posts=posts)

app.run(debug=True)