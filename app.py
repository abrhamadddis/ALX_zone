from flask import Flask
from markupsafe import escape
from flask import Flask, abort
from flask import Flask, render_template, request, url_for, flash, redirect
import datetime


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello, Bura!</h1>'


@app.route('/home/')
def about():
    return '<h3>This is a Flask web application.</h3>'


@app.route('/login/')
def login():
    return render_template('login.html', utc_dt=datetime.datetime.utcnow())


@app.route('/registor/')
def registor():
    return '<h2> this is the registration page</h2>'


@app.route('/newpost/')
def newpost():
    return '<h2> this is the new post page'



@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))



@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)


@app.route('/about/')
def about1():
    return render_template('about.html')

# ...

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)
messages = [{'title': 'Message One',
             'content': 'Message One Content'},
            {'title': 'Message Two',
             'content': 'Message Two Content'}
            ]

@app.route('/index')
def index():
    return render_template('index.html', messages=messages)

# ...

app.config['SECRET_KEY'] = 'your secret key'


# ...

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
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')