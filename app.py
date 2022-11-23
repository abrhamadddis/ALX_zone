from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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