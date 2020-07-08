from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from ItsAGramLive import ItsAGramLive
import json
from app.utils import fromPickle, toPickle, start_broadcast, stop_broadcast
base = Blueprint('base', __name__)

@base.route('/')
def login_route():
    return render_template('pages/login.html')

@base.route('/dashboard')
def info_route():
    return render_template('pages/dashboard.html',data_stream=session['data_stream'])

@base.route('/login', methods=['POST'])
def login_handle():
    live = ItsAGramLive(username=request.form['username'],password=request.form['password'])
    live.login()
    live.create_broadcast()
    # convert to pickle and store it on file
    toPickle(live)

    session['data_stream'] = {
        'broadcast_id':live.broadcast_id,
        'stream_server':live.stream_server,
        'stream_key':live.stream_key
    }
    if live.isLoggedIn:
        flash("You're not live, start broadcast after you set the server key")
        return redirect(url_for('base.info_route'))
    return redirect(url_for('base.login_route'))

@base.route('/start_broadcast')
def start():
    if start_broadcast():
        return {"status":"running","message":"You're live!!"}, 200
    else:
        return {"status":"error","message":"You're not live, start broadcast after you set the server key"}, 403

@base.route('/stop_broadcast')
def stop():
    if stop_broadcast():
        return {"status":"stopped","message":"The broadcast is ended"}, 200
    else:
        return {"status":"error","message":"something wrong here"}, 403