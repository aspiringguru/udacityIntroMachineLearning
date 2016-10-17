
import sys
import pickle
import numpy as np
import pandas as pd
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
print "# of rows = ", len(row_names), ", # of columns = ", len(col_names)

print type(data_dict['METTS MARK']['salary'])

salaries = []
incompatCount = 0
for row in row_names:
    salary = data_dict[row]['salary']
    if isinstance(salary, basestring):
        print "incompatible type"
        salaries.append(0)
        incompatCount += 1
    else:
        salaries.append(salary)
print "incompatCount=", incompatCount
print "salaries=", salaries
print "type(salaries)=", type(salaries), "type(salaries[0])=", type(salaries[0]), "len(salaries)=", len(salaries), "len(row_names)=", len(row_names)
from pandas import *
df = DataFrame({'name': row_names, 'salary': salaries})
print df
print df.shape

result = df.sort(['salary'], ascending=[True])
print "sorted DF = ", result
print result.shape

print "top 10 salaries"
print result.tail(10)

max = 0
for i in range(len(salaries)):
    if salaries[i] > max:
        max = salaries[i]
        maxIndex = i
print "max value in salaries=", max, "maxIndex=", maxIndex, "row_names=", row_names[maxIndex]

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
plt.hist(salaries, 50, normed=1, facecolor='green', alpha=0.75)
plt.grid(True)
plt.show()

#remove the outlier from salaries.
del data_dict[row_names[maxIndex]]
print row_names[maxIndex], "deleted"
row_names = data_dict.keys()
col_names = data_dict['METTS MARK'].keys()

salaries = []
incompatCount = 0
print "--------------------"
for row in row_names:
    salary = data_dict[row]['salary']
    if isinstance(salary, basestring):
        print "incompatible type"
        salaries.append(0)
        incompatCount += 1
    else:
        salaries.append(salary)
print "incompatCount=", incompatCount
print salaries
print type(salaries), type(salaries[0])
max = 0
for i in range(len(salaries)):
    if salaries[i] > max:
        max = salaries[i]
        maxIndex = i
print "max value in salaries=", max, "maxIndex=", maxIndex, "row_names=", row_names[maxIndex]

import numpy as np
import matplotlib.pyplot as plt
plt.hist(salaries, 50, normed=1, facecolor='green', alpha=0.75)
plt.grid(True)
plt.show()

