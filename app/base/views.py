from flask import Blueprint, render_template, redirect, url_for, request, session
from ItsAGramLive import ItsAGramLive
import json
from app.utils import fromPickle, toPickle
base = Blueprint('base', __name__)

@base.route('/')
def login_route():
    return render_template('pages/login.html')

@base.route('/dashboard')
def info_route():
    return render_template('pages/dashboard.html')

@base.route('/login', methods=['POST'])
def login_handle():
    live = ItsAGramLive(username=request.form['username'],password=request.form['password'])
    live.login()
    
    # convert to pickle and store it on file
    toPickle(live)
    if live.isLoggedIn:
        return redirect(url_for('base.info_route'))
    return redirect(url_for('base.login_route'))