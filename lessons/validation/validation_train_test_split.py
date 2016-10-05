"""
NB: model_selection withdrawn and superceded by cross_validation
"""

import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn import datasets
from sklearn import svm
import time

iris = datasets.load_iris()
print ("iris.data.shape=", iris.data.shape)
print ("iris.target.shape=", iris.target.shape)

start_time = time.time()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)
print("---train_test took  %s seconds ---" % (time.time() - start_time))

#http://scikit-learn.org/dev/modules/generated/sklearn.model_selection.train_test_split.html
#
print ("type(X_train)=", type(X_train))

print ("X_train.shape=", X_train.shape)
print ("y_train.shape=", y_train.shape)

print ("X_test.shape=", X_test.shape)
print ("y_test.shape=", y_test.shape)

start_time = time.time()
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
print("---svm.SVC took %s seconds ---" % (time.time() - start_time))

print ("score = ", clf.score(X_test, y_test))