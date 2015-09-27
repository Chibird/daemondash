from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
import numpy
import pickle

from flask import Flask
from flask import request
from flask import render_template
import specific_user

app = Flask(__name__, static_url_path='/static')

classifier_pickle = "classifier.pickle"
vectorizer_pickle = "vectorizer.pickle"

global current_user
current_user= ""
global num
num = -1

def logistic(value):
	return 1.0 / (1 + numpy.exp(-10*(value - 0.5)))

@app.route('/test/')
def render_fn():
	return app.send_static_file('test.html')

@app.route('/input', methods=['POST'])
def input_fn():
	if request.method == 'POST':
		global current_user
		current_user = request.form['user']
		global num
		num = request.form['num']
		return ""



@app.route('/output')
def output_fun():
	in_file = open(classifier_pickle, "r")
	classifier = pickle.load(in_file)
	in_file.close()
	in_file = open(vectorizer_pickle, "r")
	vectorizer = pickle.load(in_file)
	in_file.close()

	timeline = specific_user.get_tweets(current_user, num)
	texts = []

	for tweet in timeline:
		texts.append(tweet.text)

	return str(logistic(numpy.mean(classifier.predict(vectorizer.transform(texts))) / 4.0))

if __name__ == '__main__':
    app.run()