#!/usr/bin/python

import sys
import pickle
import numpy as np
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','salary'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)


#briefly explore content and structure
print "type(data_dict)=", type(data_dict), "len(data_dict.keys())=", len(data_dict.keys())
row_names = data_dict.keys()
print "row_names=", row_names
col_names = data_dict['METTS MARK'].keys()
print "col_names =", col_names
#now search for outliers across various columns.
param = 'salary'
maxParamValue = 0
colData = []
nanCount = 0
for row in row_names:
    temp = data_dict[row][param]
    #if isinstance(temp, basestring):
    #    nanCount += 1
    #else:
    if temp>maxParamValue: maxParamValue=temp
    colData.append(temp)
print "colData=", colData
print "nanCount", nanCount, "# of numeric values = ", len(colData)
print max(colData), min(colData)

data_dict_Values = data_dict.values()
print "data_dict.values()=", data_dict.values()
print type(temp)
data_dict_lists = []
for values in data_dict_Values:
    data_dict_lists.append(values.values())
data_dict_nparray = np.array(data_dict_lists)
print "col_names=", col_names
print "type(data_dict_nparray)=", type(data_dict_nparray)
print "data_dict_nparray.shape=", data_dict_nparray.shape
print "data_dict_nparray.shape[0]=", data_dict_nparray.shape[0]
print "data_dict_nparray=", data_dict_nparray
print "---------------------------"
#data_dict_nparray.dtype.names = col_names
#print "data_dict_nparray[0][0]=", data_dict_nparray[0][0]
#print "data_dict_nparray[0][1]=", data_dict_nparray[0][1]
#print "data_dict_nparray[0][2]=", data_dict_nparray[0][2]
print "---------------------------"
print "data_dict_nparray.dtype.names=", data_dict_nparray.dtype.names
#quikc simple plot to identify outliers
import matplotlib.pyplot as plt
temp = []
for I in len(data_dict_nparray.shape[0]):
    temp.append(data_dict_nparray[i][0])


plt.plot(temp)
plt.xlabel('Salary')
plt.ylabel('name')
plt.show()




### Task 2: Remove outliers

### Task 3: Create new feature(s)

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!
from sklearn.cross_validation import train_test_split
features_train, features_test, labels_train, labels_test = \
    train_test_split(features, labels, test_size=0.3, random_state=42)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)