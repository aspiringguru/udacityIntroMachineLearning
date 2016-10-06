#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

#preprocess(words_file = "../tools/word_data.pkl", authors_file="../tools/email_authors.pkl"):


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
print "type(features_train)=", type(features_train)
print "type(features_test)=", type(features_test)
print "type(labels_train)=", type(labels_train)
print "type(labels_test)=", type(labels_test)
print "len(labels_train)=", len(labels_train)
print "len(labels_test)=", len(labels_test)
print "labels_train=", labels_train
print "labels_test=", labels_test
print "\n"


from sklearn.naive_bayes import GaussianNB
print ("creating clf")
clf = GaussianNB()
print ("clf created. fitting")
import time
start_time = time.time()
clf.fit(features_train, labels_train)
print "--- %s seconds ---" % (time.time() - start_time)

start_time = time.time()
from sklearn.metrics import accuracy_score
print "--- time to import accuracy_score= %s seconds ---" % (time.time() - start_time)
start_time = time.time()
pred = clf.predict(features_test)
print "--- time to do prediction is %s seconds ---" % (time.time() - start_time)
print "type(pred)=", type(pred)
print "pred.shape=", pred.shape
print "type(list(pred))=", type(list(pred))
print "type(labels_test)=", type(labels_test)#list
print "len(labels_test)=", len(labels_test)

start_time = time.time()
accScore = accuracy_score(labels_test, pred)
print "--- time for accuracy_score is %s seconds ---" % (time.time() - start_time)
print "accuracy_score=", accScore
print "type(accuracy_score)=", type(accuracy_score)




#########################################################


