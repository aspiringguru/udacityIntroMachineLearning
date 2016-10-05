#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()

print "type(features_train)=", type(features_train)
print "type(features_test)=", type(features_test), "features_test.shape=", features_test.shape
print "type(vectorizer)=", type(vectorizer)
print "len(vectorizer.get_feature_names())=", len(vectorizer.get_feature_names())
print "vectorizer.get_feature_names()=", vectorizer.get_feature_names()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]


### your code goes here
#Get a decision tree up and training on the training data
#http://scikit-learn.org/stable/modules/tree.html
#http://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
#now predict values from  features_test
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
#now calculate accuracy by comparing predicted values against known values.
print "accuracy_score(labels_test, pred)=", accuracy_score(labels_test, pred) #0.947667804323

# Identify the Most Powerful Features
#feature_importances_ : array of shape = [n_features]
# The feature importances. The higher, the more important the feature.

print "type(clf.feature_importances_)=", type(clf.feature_importances_)
print "clf.feature_importances_.shape=", clf.feature_importances_.shape
print "type(clf.feature_importances_.shape[0])=", type(clf.feature_importances_.shape[0])
print "clf.feature_importances_.shape[0]=", clf.feature_importances_.shape[0]

count = 0
results = []
maxFeatImp = 0
maxCount = 0
print "__________________________"
feature_num = 0
for importance in clf.feature_importances_:
	if importance >= 0.2: #0.015:
		print "feature_num=", feature_num, "importance=", importance, "feature=", vectorizer.get_feature_names()[feature_num]
	feature_num += 1


#http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.argmax.html
#ndarray.argmax(axis=None, out=None) Return indices of the maximum values along the given axis.
#http://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html#numpy.argmax
print "__________________________"
#this returns 36327 0.764705882353 sshacklensf
#correct answers are 0.764705882353 & 33614 & sshacklensf

#weird to have two of 3 correct answers. perhaps the pickle generated by a previous routine
# and losted for this exercise is different to others?

X = []
Y = []
feature_num = 0
for importance in clf.feature_importances_:
    #print feature_num, importance, vectorizer.get_feature_names()[feature_num]
    X.append(importance)
    Y.append(feature_num)
    feature_num += 1

import matplotlib.pyplot as plt
plt.scatter(X, Y)
plt.show()


"""
results after using plot to show distribution of importances.

selected cutoff point @ 0.015 to enable showing these outliers

feature_num= 20865 importance= 0.0749500333111 feature= fyi
feature_num= 31857 importance= 0.0263157894737 feature= pm
feature_num= 35875 importance= 0.134028294862 feature= smith
feature_num= 36327 importance= 0.764705882353 feature= sshacklensf

still can't see how to get the same number as 'correct' solution.


after returning to vectorize_text.py and adding sshacklensf to wordsToRemove.

feature_num= 14774 importance= 0.666666666667 feature= cgermannsf


"""