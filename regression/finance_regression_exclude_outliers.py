#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    


import sys
import pickle
import time

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

start_time = time.time()
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )
print("---time to load pickle = %s seconds ---" % (time.time() - start_time))
### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]

start_time = time.time()
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
print("---time to do featureFormat = %s seconds ---" % (time.time() - start_time))

start_time = time.time()
target, features = targetFeatureSplit( data )
print("---time to do targetFeatureSplit = %s seconds ---" % (time.time() - start_time))

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
start_time = time.time()
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
print("---time to do train_test_split = %s seconds ---" % (time.time() - start_time))
train_color = "b"
test_color = "r"#was originally 'b'

### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.

#from Extracting Slope and Intercept
#Import LinearRegression from sklearn, and create/fit your regression.
from sklearn.linear_model import LinearRegression
reg = LinearRegression()
start_time = time.time()
reg.fit(feature_train, target_train)
print("---time to do reg.fit = %s seconds ---" % (time.time() - start_time))

#Extract the slope (stored in the reg.coef_ attribute) and the intercept.
print "type(reg.coef_)=", type(reg.coef_)
print "slope = reg.coef_ = ", reg.coef_
print "type(reg.intercept_)=", type(reg.intercept_)
print reg.intercept_

start_time = time.time()
trainScore = reg.score(feature_train, target_train)
print("---time to do reg.score = %s seconds ---" % (time.time() - start_time))
print "type(trainScore)=", type(trainScore)
print "trainScore=", trainScore

start_time = time.time()
testScore = reg.score(feature_test, target_test)
print("---time to do reg.score = %s seconds ---" % (time.time() - start_time))
print "type(testScore)=", type(testScore)
print "testScore=", testScore




### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass
reg.fit(feature_test, target_test)
print "outliers excluded slope = reg.coef_ = ", reg.coef_
plt.plot(feature_train, reg.predict(feature_train), color="b")
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
