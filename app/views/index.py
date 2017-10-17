#!/usr/bin/python3
from app import app

from flask import render_template


@app.route('/index')
@app.route('/')
def index():
    user = {'username': 'xia.hua'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',titles="Home",user=user,posts=posts)




