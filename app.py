from flask import Flask, render_template

app = Flask(__name__)


<<<<<<< HEAD
=======
@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
>>>>>>> 45f7dacc75c04722d3156a758c5823a5661fb222

=======
>>>>>>> dcf303f62f165dc4e454172f18bb140a5f22dd5e
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