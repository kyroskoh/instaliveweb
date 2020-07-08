from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'very_secret_you_cant_even_break_it'
    # Routes
    from app.base.views import base
    
    # Blueprint
    app.register_blueprint(base)
    
    return app