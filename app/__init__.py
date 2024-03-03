from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    from app.routes.home import home_blueprint
    app.register_blueprint(home_blueprint)
    

    return app