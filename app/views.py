from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Carlos'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },
		{ 
            'author': {'nickname': 'Juan'}, 
            'body': 'El mundo es un pañuelo' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)