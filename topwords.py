import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
import nltk
import specific_user
import numpy
import tweepy
import re

def top_words(classifier, vectorizer, timeline, n):
	word_total = ""
	for tweet in timeline:
		word_total += tweet.text + " "
	tokens = word_total.split(" ")
	stopset = set(nltk.corpus.stopwords.words("english"))
	
	new_tokens = []
	for word in tokens:
		if re.match("^([a-zA-Z]+)$", word) != None:
			new_tokens.append(word.lower())

	for word in stopset:
		while (word in new_tokens):
			new_tokens.remove(word)

	freq_dist = nltk.FreqDist(new_tokens)
	most_common = freq_dist.most_common(n)

	words = []
	for (word, number) in most_common:
		words.append(word)

	sentiments = classifier.predict(vectorizer.transform(words))
	for i in range(0, len(words)):
		words[i] = (words[i], sentiments[i])

	return words