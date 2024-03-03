from flask import render_template, Blueprint


home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/',)
def home():
    return render_template('home.html')