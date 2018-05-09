#!/usr/bin/env python

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, escape
import os

app = Flask(__name__)

app.config.from_object('configmodule.DefaultConfig')
if "CONFIG_FILE" in os.environ:
  app.config.from_envvar('CONFIG_FILE')

app.secret_key = app.config['SECRET_KEY']

@app.route("/")
def hello():
    return "Hello World!"

def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
