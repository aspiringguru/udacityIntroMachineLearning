
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

myDF = pd.DataFrame(index=row_names, columns=col_names)
print "#rows in dataframe = len(myDF.index)=", len(myDF.index)
myDF.columns = col_names
print "-------------"
print myDF.head(n=3)

count = 0
for row in row_names:
    count += 1
    if count>3: break
    temp = data_dict[row]
    #print "type=", type(temp), "type(temp.values())=", type(temp.values()), "len(temp.values())=", \
    #    len(temp.values()), "len(col_names)=", len(col_names)
    print "temp.values()=", temp.values()
    df2 = pd.DataFrame(temp.values())
    myDF.append(df2)
print "-------------"
print myDF.head(n=3)
print "myDF.shape=", myDF.shape
