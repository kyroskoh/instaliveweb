from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from InstaLiveCLI import InstaLiveCLI
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
    live = InstaLiveCLI(username=request.form['username'],password=request.form['password'])
    login_status = live.login()

    if login_status:
        live.create_broadcast()
        
        session['settings'] = live.settings

        session['data_stream'] = {
            'broadcast_id':live.broadcast_id,
            'stream_server':live.stream_server,
            'stream_key':live.stream_key,
            'status':'Idle',
        }

        return redirect(url_for('base.info_route'))

    
    flash('Username or Password incorrect!')

    return redirect(url_for('base.login_route'))

@base.route('/start_broadcast')
def start():
    if start_broadcast():
        session['data_stream']['status'] = 'Running'
        return {"status":"running","message":"You're live!!"}, 200
    else:
        return {"status":"error","message":"You're not live, start broadcast after you set the server key"}, 403

@base.route('/stop_broadcast')
def stop():
    if stop_broadcast():
        session['data_stream']['status'] = 'Stopped'
        return {"status":"stopped","message":"The broadcast is ended"}, 200
    else:
        return {"status":"error","message":"something wrong here"}, 403