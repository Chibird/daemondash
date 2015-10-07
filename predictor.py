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
import topwords

app = Flask(__name__, static_url_path='/static')

classifier_pickle = "classifier.pickle"
vectorizer_pickle = "vectorizer.pickle"

global current_user
current_user= ""
global num
num = -1
global timeline
timeline = None

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

	global timeline
	timeline = specific_user.get_tweets(current_user, num)
	texts = []

	for tweet in timeline:
		texts.append(tweet.text)

	lst = topwords.top_words(classifier, vectorizer, timeline, 10)
	long_str = ""
	for w in lst:
		# print rating
		long_str += w[0] + " " + str(w[1]) + " "
	print long_str

	return str(logistic(numpy.mean(classifier.predict(vectorizer.transform(texts))) / 4.0)) + " " + long_str

# @app.route('/outputwords')
# def output_fun2():
# 	in_file = open(classifier_pickle, "r")
# 	classifier = pickle.load(in_file)
# 	in_file.close()
# 	in_file = open(vectorizer_pickle, "r")
# 	vectorizer = pickle.load(in_file)
# 	in_file.close()

# 	while(timeline == None):
# 		print("")
# 	print(len(timeline))
# 	lst = topwords.top_words(classifier, vectorizer, timeline, 10)
# 	print("fdsafds")
# 	long_str = ""
# 	for (word, rating) in lst:
# 		long_str += word + " " + rating
# 	print(long_str)
# 	return(long_str)

if __name__ == '__main__':
    app.run()