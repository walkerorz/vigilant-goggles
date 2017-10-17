#!/usr/bin/python3
from flask import render_template, flash, redirect
from app import app
from app.models.Login import LoginForm

@app.route('/login',methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for openid = '+ form.openid.data,'remember_me = ' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',form=form)

