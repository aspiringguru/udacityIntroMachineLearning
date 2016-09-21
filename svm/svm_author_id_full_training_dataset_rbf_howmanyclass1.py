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
#########################################################
### your code goes here ###
##config start
c = 10000
fractionTest = 1.0
##config end
from datetime import datetime
start=datetime.now()
print "preprocessing..."
features_train, features_test, labels_train, labels_test = preprocess()
print "preprocessing time = ",datetime.now()-start, "------------"

print "len(features_test)=", len(features_test)
print "type(len(features_test))=", type(len(features_test))
print "features_test[10]=", features_test[10], "type(features_test[10])=", type(features_test[10])
print list(features_test[10])
print len(features_test[10])
print "labels_test[10]=", labels_test[10]
print "type(features_test)=", type(features_test)
print "features_test.shape=", features_test.shape


#features_train = features_train[:len(features_train)*fractionTest]
#labels_train = labels_train[:len(labels_train)*fractionTest]

from sklearn.svm import SVC
print ("loading SVC kernel")
start=datetime.now()
#http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
clf = SVC(C=c, kernel="rbf")
print "time to load kernel = ",datetime.now()-start, "------------"
print "fitting"
start=datetime.now()
clf.fit(features_train, labels_train)
print "fitting time = ",datetime.now()-start, "------------"
countChris = 0
countNotChris = 0
for i in range(len(features_test)):
    pred = clf.predict([features_test[i]])
    if pred[0].item() == 1:
        countChris += 1
        print "pred[", i, "] is 1, a chris, countChris=", countChris
    else:
        countNotChris += 1
        print "pred[", i, "] is 0, not chris, countNotChris=", countNotChris
print "countChris =", countChris, "countNotChris =", countNotChris

#########################################################
