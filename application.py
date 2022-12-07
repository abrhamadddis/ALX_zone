#!/usr/bin/python3
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort, session
from datetime import datetime

application = Flask(__name__)
application.config['SECRET_KEY'] = 'd6bb525dd12c9953922f61784e785ba147f643b5d515ba0f'
def get_db_connection():
    conn = sqlite3.connect('test.db')
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

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        user = request.form['email']
        password = request.form['password']
        session['user'] = user
        if not user:
            flash('please enter your username')
        elif not password:
            flash('please enter your password')
        else:
            conn = get_db_connection()
            output = conn.execute("SELECT name, password FROM  user where name= '"+user+"' and password='"+password+"'").fetchall()
            if len(output) == 0:
                flash("User not found please signup")
            else:
                return redirect(url_for('post'))

    return render_template('login.html')

@application.route('/register/', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
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
                         (name, email, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
    return render_template('register.html')

@application.route('/createpost/', methods=('GET', 'POST'))
def createpost():
        user = session['user']
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            if not title:
                flash('Title is required!')
            elif not content:
                flash('Content is required!')
            else:
                now = datetime.now()
                formatted_date = now.strftime('%Y-%m-%d')
                conn = get_db_connection()
                conn.execute('INSERT INTO posts (created, title, content, created_by) VALUES (?, ?, ?, ?)',
                            (formatted_date, title, content, user))
                conn.commit()
                conn.close()
                return redirect(url_for('post'))
        return render_template('update_post.html', user=user)

@application.route('/<int:id>/edit/', methods=('GET', 'POST'))
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

@application.route('/posts/')
def post():
    if 'user' in session:
        conn=get_db_connection()
        posts=conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return render_template('posts.html', posts=posts)
    else:
        return redirect(url_for('login'))

@application.route('/logout/', methods=('GET', 'POST'))
def logout():
    session.pop("user", None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    application.run(debug=True)