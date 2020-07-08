from flask import Flask

def create_app():
    app = Flask(__name__)

    # Routes
    from app.base.routes import base
    
    # Blueprint
    app.register_blueprint(base)
    
    return app