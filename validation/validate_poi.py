#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""
from time import time

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)#original
#data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson13_keys.pkl')
#

labels, features = targetFeatureSplit(data)



### it's all yours from here forward!  
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
#'acc=', 0.98947368421052628   accepted by grader

#validation 18 of 18 Deploying a Training/Testing Regime
#hold out 30% of the data for testing and set the random_state parameter to 42
#from sklearn.model_selection import train_test_split
from sklearn.cross_validation import train_test_split


start_time = time()
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)
print("--- time to train_test_split %s seconds ---" % (time() - start_time))
print "type(X_train)=", type(X_train), len(X_train)
print "type(X_test)=", type(X_test), len(X_test)
print "type(y_train)=", type(y_train), len(y_train)
print "type(y_test)=", type(y_test), len(y_test)

start_time = time()
clf = clf.fit(X_train, y_train)
print("--- time to clf.fit %s seconds ---" % (time() - start_time))


acc =  clf.score(X_test, y_test)
print ("acc=", acc)

#'acc=', 0.72413793103448276, accepted by grader.
