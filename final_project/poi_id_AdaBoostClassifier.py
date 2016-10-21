
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
start_time = time.time()
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)
print("--- time to load pickle = %s seconds ---" % (time.time() - start_time))
# quick analysis shows 'TOTAL' is an outlier.
del data_dict['TOTAL']
row_names = data_dict.keys()
col_names = data_dict['METTS MARK'].keys()
#delete 'email_address' from list because we won't be using it.
del col_names[col_names.index('email_address')]
del col_names[col_names.index('poi')]
print "col_names =",col_names

#now analyse using Naive Bayes method
#sample code from
#http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html
#

import numpy as np
import types

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=2)
#arrange data from data_dict to X,Y where X,Y are np.array.
#X = input variables (), Y = predicted variable. (poi)
import pandas as pd
df = pd.DataFrame()
poi = []
for row in row_names:
    rowDict = data_dict[row]
    del rowDict['email_address']
    #print type(rowDict['poi'])#bool
    #print rowDict['poi'], type(rowDict['poi'])#type poit = bool
    poi.append(rowDict['poi'])
    del rowDict['poi']
    #print "type(rowDict)=", type(rowDict)#<type 'dict'>
    values = rowDict.values()
    #print "type(values)=", type(values)#list
    tempdict = {}
    for i in range(len(values)):
        if isinstance(values[i], basestring):
            values[i] = np.nan
            #need to think through how to handle NaN's
        rowDict[col_names[i]] = values[i]
    #print "values=", values
    #now assign list values to dictionary
    #print "\n @ row=", row, ", tempdict=", tempdict
    df = df.append(rowDict, ignore_index=True)
print "df.shape=", df.shape
print df.head(5)
print "poi=", poi

print "are there any null values = ", df.isnull().values.any()  #True
print "number of null values = ", df.isnull().sum().sum()       #1318
df.fillna(0, inplace=True)
#http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.fillna.html
#inplace=True required to modify
print "are there any null values = ", df.isnull().values.any()  #True
print "number of null values = ", df.isnull().sum().sum()       #1318

#print "type(df['restricted_stock_deferred'])=", type(df['restricted_stock_deferred'])
#print df['restricted_stock_deferred']
#print df['restricted_stock_deferred'][0:5]
#print type(df['restricted_stock_deferred'][0])

#poi = {True:1, False:0}
#NB: code above converts poi column from boolean to float64.
# don't need to convert using df = df.replace('colName':dict)

#convert to numpy array for scikit-learn pacakges
data_np = pd.DataFrame.as_matrix(df)
# need to move 'poi' column to end to suit the range columns selections below.
print "data_np.shape", data_np.shape #(145L, 19L)
#for i in range(len(col_names)):
#    print "\n", col_names[i], " = col #",i," = ", data_np[:5, i]

# convert poi values from boolean to int so scikit-kearn can process.
print type(poi[0])
for i in range(len(poi)):
    if poi[i]:
        poi[i] = 1
    else:
        poi[i] = 0
print "poi = ", poi
print len(poi) #145
#transform poi from list into numpy array one column wide.

data_np_train, data_np_test, poi_train, poi_test = train_test_split(data_np, poi, test_size=0.33, random_state=42)

from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
#http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html
#http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
print "initialising AdaBoostClassifier"
start_time = time.time()
ada = AdaBoostClassifier(base_estimator = RandomForestClassifier(n_estimators = 20, criterion = 'entropy'), algorithm = 'SAMME.R')
print("--- time to initialise AdaBoostClassifier %s seconds ---" % (time.time() - start_time))

#AdaBoostClassifier : algorithm : {'SAMME', 'SAMME.R'}, optional (default='SAMME.R')
#n_estimators : integer, optional (default=10)  The number of trees in the forest.
#criterion : string, optional (default="gini") Supported criteria are "gini" for the Gini impurity and "entropy" for the information gain
#algorithm


#now fit model using data from data_np_train.
#NBB: need to split into train and test datasets with scikit-learn package.


print "data_np_train.shape = ", data_np_train.shape
print "len(poi_train) = ", len(poi_train)
start_time = time.time()
ada.fit(data_np_train, poi_train)
print("--- time to fit AdaBoostClassifier %s seconds ---" % (time.time() - start_time))

#now predict values using the test dataset. [all rows except the last column]
start_time = time.time()
predictions = ada.predict(data_np_test)#needs test set here.
print("--- time to predict AdaBoostClassifier %s seconds ---" % (time.time() - start_time))

print "type(predictions)=", type(predictions)

#now score the accuracy, use all rows except last column from input data, compare to last column.

start_time = time.time()
score = ada.score(data_np_test, poi_test)
print("--- time to score AdaBoostClassifier %s seconds ---" % (time.time() - start_time))

print "type(score)=", type(score)
print 'Accuracy:', "%.2f" %(score*100)+'%'

#ada = AdaBoostClassifier()#created previously
from sklearn.metrics import confusion_matrix
#http://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html

start_time = time.time()
cm = confusion_matrix(data_np_test[:,-1], predictions )
print("--- time to calc confusion_matrix %s seconds ---" % (time.time() - start_time))
print "type(cm)", type(cm)
print "cm=", cm
cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
print "type(cm_normalized)=", type(cm_normalized)
print "cm_normalized=", cm_normalized
print "True Positive = ", cm_normalized[0,0]
print "False Negative = ", cm_normalized[0,1]
print "False Positive = ", cm_normalized[1,0]
print "True Negative = ", cm_normalized[1,1]
#something not right as TP = FP = 1.0 & FN = TN = 0.0.

