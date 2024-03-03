# Author: Muhammad Sallar Bin Aamir

from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
import pandas as pd

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
data = pd.read_csv('app\data\IMDBDataset.csv')

X = data['review']
y = data['class']

stop_words = set(stopwords.words('english'))
porter = PorterStemmer()


def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [porter.stem(token) for token in tokens if token.isalpha() and token not in stop_words]
    return " ".join(tokens)

X_preprocessed = X.apply(preprocess_text)


vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X_preprocessed)


X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)


classifier = MultinomialNB(alpha=0.1)
classifier.fit(X_train, y_train)

predictions = classifier.predict(X_test)

def show_metrics():
    accuracy = accuracy_score(y_test, predictions)
    precision = precision_score(y_test, predictions, average='macro')
    recall = recall_score(y_test, predictions, average='macro')
    return accuracy, precision, recall


def predict_review(review):
    review = vectorizer.transform([review])
    prediction = classifier.predict(review)
    return prediction[0]


