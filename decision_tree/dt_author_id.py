#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels

features_train, features_test, labels_train, labels_test = preprocess()

#find the number of features in your data.
print ("type(features_train)=", type(features_train))
print ("type(features_test)=", type(features_test))
print ("type(labels_train)=", type(labels_train))
print ("type(labels_test)=", type(labels_test))

print ("len(features_train[0])=", len(features_train[0]))

#########################################################
### your code goes here ###
#Get the decision tree up and running as a classifier,
# setting min_samples_split=40.
# It will probably take a while to train.
# Whats the accuracy?
from sklearn import tree
clf = tree.DecisionTreeClassifier()
start_time = time()
clf = clf.fit(features_train, labels_train)
print("--- time to clf.fit %s seconds ---" % (time() - start_time))

start_time = time()
acc =  clf.score(features_test, labels_test)
print("--- time to clf.score %s seconds ---" % (time() - start_time))
print ("acc from tree.DecisionTreeClassifier = ", acc)

#########################################################


