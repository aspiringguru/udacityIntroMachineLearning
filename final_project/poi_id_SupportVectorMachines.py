
import sys
import pickle
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
import time
sys.path.append("../tools/")

from pandas import *
import matplotlib.pyplot as plt

#from feature_format import featureFormat, targetFeatureSplit
#from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)
# quick analysis shows 'TOTAL' is an outlier.
del data_dict['TOTAL']
row_names = data_dict.keys()
col_names = data_dict['METTS MARK'].keys()
print "col_names =",col_names

#now analyse using Naive Bayes method
#sample code from
#http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html

import numpy as np
from sklearn.svm import SVC
clf = SVC(kernel="linear")
#arrange data from data_dict to X,Y where X,Y are np.array.
#X = input variables (), Y = predicted variable. (poi)
poiCol = []
salaryCol = []
total_paymentsCol = []
exercised_stock_optionsCol = []
for row in row_names:
    poi = data_dict[row]["poi"]
    #NB: poi column is True/False
    poiCol.append(poi)
    #
    salary = data_dict[row]["salary"]
    #print "row=", row, "salary=", salary
    if isinstance(salary, basestring):
        # print "incompatible type"
        salaryCol.append(0)
    else:
        salaryCol.append(salary)
    #
    total_payments = data_dict[row]["total_payments"]
    if isinstance(total_payments, basestring):
        # print "incompatible type"
        total_paymentsCol.append(0)
    else:
        total_paymentsCol.append(total_payments)
    exercised_stock_options = data_dict[row]["exercised_stock_options"]
    if isinstance(exercised_stock_options, basestring):
        # print "incompatible type"
        exercised_stock_optionsCol.append(0)
    else:
        exercised_stock_optionsCol.append(exercised_stock_options)

#quick visual display for audit/verification purposes.
print "poiCol=", poiCol
print "salaryCol=", salaryCol
print "total_paymentsCol=", total_paymentsCol
print "exercised_stock_options=", exercised_stock_optionsCol
print "------------"
print "len(poiCol)=", len(poiCol)
print "len(salaryCol)=", len(salaryCol)
print "len(total_paymentsCol)=", len(total_paymentsCol)
print "len(exercised_stock_optionsCol)=", len(exercised_stock_optionsCol)
#NB: checked all these arrays are same length.
#now construct numpy array X = ([list of points composed from columns of interest])
# ie X= ([list of points composed from salaryCol, total_paymentsCol, exercised_stock_optionsCol])
X = []
Y = []
for row in row_names:
    poi = data_dict[row]["poi"]
    if poi:
        poi = 1
    else:
        poi = 0
    salary = data_dict[row]["salary"]
    if isinstance(salary, basestring):
        salary = 0
    total_payments = data_dict[row]["total_payments"]
    if isinstance(total_payments, basestring):
        total_payments = 0
    exercised_stock_options = data_dict[row]["exercised_stock_options"]
    if isinstance(exercised_stock_options, basestring):
        exercised_stock_options = 0
    from_poi_to_this_person = data_dict[row]["from_poi_to_this_person"]
    if isinstance(from_poi_to_this_person, basestring):
        from_poi_to_this_person = 0
    from_this_person_to_poi = data_dict[row]["from_this_person_to_poi"]
    if isinstance(from_this_person_to_poi, basestring):
        from_this_person_to_poi = 0
    # = [salary, total_payments, exercised_stock_options]
    #x = [total_payments, exercised_stock_options]
    #x = [total_payments]
    #x=[salary]
    x = [exercised_stock_options]
    #x = [from_this_person_to_poi]
    #x = [from_poi_to_this_person]
    X.append(x)
    Y.append(poi)
print "Y=", Y
print "len(Y)=", len(Y), "sum(Y)=", sum(Y), "1-sum(Y)/len(Y)=", 1-sum(Y)/(1.0*len(Y))
a_train, a_test, b_train, b_test = train_test_split(X, Y, test_size=0.33, random_state=42)
print "type(a_train)=", type(a_train), "len(a_train)=", len(a_train), "len(a_train[0])=", len(a_train[0])
print "type(a_test)=", type(a_test), "len(a_test)=", len(a_test)
print "type(b_train)=", type(b_train), "len(b_train)=", len(b_train)\
#print "len(b_train[0])=", len(b_train[0])
print "sum(b_train)=", sum(b_train), "1-sum(b_train)/len(b_train)=", 1-sum(b_train)/(1.0*len(b_train))
print "type(b_test)=", type(b_test), "len(b_test)=", len(b_test), "sum(b_test)=", sum(b_test), "1-sum(b_test)/len(b_test)=", 1-sum(b_test)/(1.0*len(b_test))

print "clf.fitting"
start_time = time.time()
clf.fit(a_train, b_train)
print("--- clf.fitting time = %s seconds ---" % (time.time() - start_time))
print "clf.fitted, clf.predicting"
start_time = time.time()
b_pred = clf.predict(a_test)
print("--- clf.predicting time = %s seconds ---" % (time.time() - start_time))
print "b_test=", b_test
print "b_pred=", b_pred
print "accuracy_score=", accuracy_score(b_test, b_pred)
print "clf.score(X, Y)=", clf.score(a_train, b_train)


#when x = [salary, total_payments, exercised_stock_options]
#clf.score(X, Y)= 0.868965517241

#when x = [total_payments, exercised_stock_options]
#clf.score(X, Y)= 0.875862068966

#NB: removing salary increases the accuracy of prediction.
#when x = [total_payments]
#clf.score(X, Y)= 0.868965517241

#when x = [exercised_stock_options]
#clf.score(X, Y)= 0.875862068966

#when x = [from_poi_to_this_person]
#clf.score(X, Y)= 0.862068965517

#when x=[salary]
# clf.score(X, Y)= 0.875862068966

#when x = [from_this_person_to_poi]
#clf.score(X, Y)= 0.848275862069