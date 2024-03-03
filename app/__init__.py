from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes.home import home_blueprint
    app.register_blueprint(home_blueprint)
    

    return app