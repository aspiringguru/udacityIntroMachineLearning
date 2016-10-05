#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""
from time import time

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
print "type(labels)=", type(labels), "len(labels)=", len(labels)
print "type(features)=", type(features), "len(features)=", len(features)



### your code goes here 
from sklearn import tree

start_time = time()
clf = tree.DecisionTreeClassifier()
print("--- time to initialise tree.DecisionTreeClassifier %s seconds ---" % (time() - start_time))

start_time = time()
clf = clf.fit(features, labels)
print("--- time to clf.fit %s seconds ---" % (time() - start_time))

start_time = time()
acc =  clf.score(features, labels)
print("--- time to clf.score %s seconds ---" % (time() - start_time))

print ("acc=", acc)

#validation 18 of 18 Deploying a Training/Testing Regime
#hold out 30% of the data for testing and set the random_state parameter to 42
#from sklearn.model_selection import train_test_split
from sklearn.cross_validation import train_test_split


#step1 : split the data into train/test.
start_time = time()
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
print("--- time to train_test_split %s seconds ---" % (time() - start_time))
print "type(X_train)=", type(X_train), len(X_train)
print "type(X_test)=", type(X_test), len(X_test)
print "type(y_train)=", type(y_train), len(y_train)
print "type(y_test)=", type(y_test), len(y_test)

#step 2 : fit the classigied with the training data
start_time = time()
clf = clf.fit(X_train, y_train)
print("--- time to clf.fit %s seconds ---" % (time() - start_time))
print "type(clf)=", type(clf)

#step 3: test the accuracy of the fitted classifier using the test data.
acc =  clf.score(X_test, y_test)
print ("acc=", acc)

#----------------------------------------------------------
# Number of POIs in Test Set

# step1 : run classifier prediction.
predicted = clf.predict(X_test)
print "type(predicted)=", type(predicted)

# step 2 : look at result type and contents.
import numpy as np
print np.array(y_test)

# step 3 : find number of predicted POI's.
#ie : count elements with value 1.0
print len([e for e in y_test if e == 1.0])

#ans = 4, accepted by grader.

print "len(y_test)=", len(y_test)
#----------------------------------------------------------

#Use the precision_score and recall_score available in sklearn.metrics to compute those quantities.
#http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html
from sklearn.metrics import precision_score
precScore = precision_score(X_test, y_test, average='macro')
print "precScore=", precScore

#UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 in labels with no predicted samples.


#http://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html
from sklearn.metrics import recall_score
recScore = recall_score(X_test, y_test, average='macro')
print "recScore=", recScore
#UndefinedMetricWarning: Recall is ill-defined and being set to 0.0 in labels with no true samples.

