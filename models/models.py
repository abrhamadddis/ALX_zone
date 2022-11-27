from flask import Flask,render_template
from flask_sqlalchemy import flask_sqlalchemy
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)

class Author(db.model):
    __tablename__= 'author' 
    user_id = db.Column(db.BIGINT,primary_key =True) 
    firstname = db.Column(db.VARCHAR(25),unique=True,nullable=False)
    lastname = db.Column(db.VARCHAR(25),unique=True,nullable=False)
    email =  db.Column(db.VARCHAR(25),unique=True,nullable=False)
    password = db.Column(db.VARCHAR(25),nullable=False)
    image = db.Column(db.VARBYTE(MAX),nullable=False,default= None)
    blog = db.relationship('Blog',backref='author',lazy=True)
    comment = db.relationship('Comment',backref='author',lazy=True)
def __rep__(self):
    """returns the object representation in string format"""
    return f"Author('{self.firstname}',{self.email}','{self.image}'"

class Blog(db.model):
    __tablename__='blog'
    blog_id = db.Column(db.BIGINT,primary_key =True) 
    title = db.Column(db.VARCHAR(200),nullable=False)
    content = db.Column(db.TEXT,nullable=False)
    user_id = db.Column(db.BIGINT,db.Foreignkey('user_id'),nullable=False)
    created_date =db.Column(db.DateTime,nullable=False,default = datetime.now())
    comment = db.relationship('Comment',backref='blog',lazy=True)
def __rep__(self):
    """returns the object representation in string format"""
    return f"Blog('{self.title}','{self.created_date}'"
class Comment(db.model):
    __tablename__='comment'
    blog_id = db.Column(db.BIGINT,db.Foreignkey('blog_id'),nullable=False)
    user_id =  user_id = db.Column(db.BIGINT,db.Foreignkey('user_id'),nullable=False)
    comment = db.Column(db.TEXT,)
    date_created = db.Column(db.DateTime.now())

def __rep__(self):
    """returns the object representation in string format"""
    return f"Comment('{self.comment}','{self.date_created}'"
