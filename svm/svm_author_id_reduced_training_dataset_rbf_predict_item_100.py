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

print "features_test[10]=", features_test[10], "type(features_test[10])=", type(features_test[10])
print list(features_test[10])
print len(features_test[10])
print "labels_test[10]=", labels_test[10]
print "type(features_test)=", type(features_test)
print "features_test.shape=", features_test.shape


print "reduce size of features_train set from ", len(features_train)
features_train = features_train[:len(features_train)/100]
print "reduce size of labels_train set from ", len(labels_train )
labels_train = labels_train[:len(labels_train)/100]

#########################################################
### your code goes here ###
def testAccuracy(c):
    from sklearn.svm import SVC
    print ("loading SVC kernel")
    start=datetime.now()
    #clf = SVC(kernel="linear")
    #http://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html
    clf = SVC(C=c, kernel="rbf")
    print "time to load kernel = ",datetime.now()-start, "------------"
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
    print "acc = ", acc
    pred = clf.predict([features_test[10]])
    print "prediction for element 10 = ", pred
    pred = clf.predict([features_test[26]])
    print "prediction for element 26 = ", pred
    pred = clf.predict([features_test[50]])
    print "prediction for element 50 = ", pred
    return acc

result = testAccuracy(10000)
print "\nat c=10000, accuracy = ", result, "\n"

"""
result = testAccuracy(10)
print "\nat c=10, accuracy = ", result, "\n"
result = testAccuracy(100)
print "\nat c=100, accuracy = ", result, "\n"
result = testAccuracy(1000)
print "\nat c=1000, accuracy = ", result, "\n"
result = testAccuracy(10000)
print "\nat c=10000, accuracy = ", result, "\n"
"""
#########################################################


"""
with 1% of training set.
at c=10, accuracy =  0.616040955631
at c=100, accuracy =  0.616040955631
at c=1000, accuracy =  0.821387940842
at c=10000, accuracy =  0.892491467577


with 100% of training set
at c=10, accuracy =  0.810580204778
at c=100, accuracy =  0.955062571104
at c=1000, accuracy =  0.982935153584
at c=10000, accuracy =  0.990898748578


"""