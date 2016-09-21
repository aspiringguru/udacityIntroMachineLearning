#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
from datetime import datetime
start=datetime.now()
print "preprocessing..."
features_train, features_test, labels_train, labels_test = preprocess()
print "preprocessing time = ",datetime.now()-start, "------------"



#########################################################
### your code goes here ###
from sklearn.svm import SVC
print ("loading SVC kernel")
start=datetime.now()
clf = SVC(kernel="linear")
print "preprocessing time = ",datetime.now()-start, "------------"
print "fitting"
start=datetime.now()
clf.fit(features_train, labels_train)
print "fitting time = ",datetime.now()-start, "------------"
print "fitted, predicting"
start=datetime.now()
pred = clf.predict(features_test)
print "predicting time = ",datetime.now()-start, "------------"
from sklearn.metrics import accuracy_score
print "calculating accuracy"
start=datetime.now()
acc = accuracy_score(pred, labels_test)
print "calculating accuracy time = ",datetime.now()-start, "------------"
print ("acc = ", acc)

#########################################################


