from flask import Blueprint, render_template, redirect, url_for, request

base = Blueprint('base', __name__)

@base.route('/')
def login_route():
    return render_template('pages/login.html')

@base.route('/dashboard')
def info_route():
    return render_template('pages/dashboard.html')

@base.route('/login', methods=['POST'])
def login_handle():
    print(request.form)
    return redirect(url_for('base.login_route'))