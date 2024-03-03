from flask import render_template, Blueprint, request
from app.scripts.classifier import predict_review, show_metrics


home_blueprint = Blueprint('home', __name__)

@home_blueprint.route('/',)
def home():
    return render_template('home.html')

@home_blueprint.route('/classify', methods=['GET', 'POST'])
def classify():
    if request.method == 'POST':
        review = request.form['review']
        prediction = predict_review(review)
        accuracy, precision, recall = show_metrics()
        return render_template('result.html', prediction=prediction, accuracy=accuracy, precision=precision, recall=recall)
    return render_template('home.html')