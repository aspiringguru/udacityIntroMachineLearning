
import sys
import pickle
import numpy as np
import pandas as pd
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
row_names = data_dict.keys()
# quick analysis shows 'TOTAL' is an outlier.
del data_dict['TOTAL']
col_names = data_dict['METTS MARK'].keys()
print "col_names =",col_names

#after removing the outlier 'TOTAL' we can see three people with salaries significantly higher than the rest
# but not out of range by order of magnitude.

#--------------------------------------------------------------------------------------------

#now we see the 'total_payment' to 'LAY KENNETH L' is an outlier and significently larger than alternatives.
#--------------------------------------------------------------------------------------------

def showColumnOutliers(colName, data_dict):
    print "colName=", colName
    row_names = data_dict.keys()
    colData = []
    incompatCount = 0
    for row in row_names:
        col = data_dict[row][colName]
        if isinstance(col, basestring):
            # print "incompatible type"
            colData.append(0)
            incompatCount += 1
        else:
            colData.append(col)

    print "incompatCount=", incompatCount
    print "colData=", colData
    print "type(colData)=", type(colData), "type(colData[0])=", type(colData[0]), "len(colData)=", len(colData), "len(row_names)=", len(row_names)
    df = DataFrame({'name': row_names, 'colName': colData})
    # print df
    print "df.shape as loaded, no cleaning."
    print df.shape
    print "deleting rows with Salary == 0"
    df = df[df.colName != 0]
    print df.shape

    # result = df.sort(['salary'], ascending=[True])
    result = df.sort_values(by=['colName'], ascending=[True])
    # print "sorted DF = ", result
    print "result.shape=", result.shape

    print "top 10 values for",colName
    print result.tail(10)
    # print "result['salary']=", result['salary']
    print type(result['colName'])
    print type(list(result['colName']))

    plt.hist(list(result['colName']), 50, normed=1, facecolor='green', alpha=0.75)
    plt.title("frequency distribution of "+colName)
    plt.grid(True)
    plt.show()

showColumnOutliers('salary', data_dict)
showColumnOutliers('deferral_payments', data_dict)
showColumnOutliers('total_payments', data_dict)
showColumnOutliers('exercised_stock_options', data_dict)
showColumnOutliers('bonus', data_dict)
showColumnOutliers('restricted_stock', data_dict)
showColumnOutliers('restricted_stock_deferred', data_dict)
showColumnOutliers('total_stock_value', data_dict)
showColumnOutliers('expenses', data_dict)
showColumnOutliers('loan_advances', data_dict)
showColumnOutliers('from_messages', data_dict)
showColumnOutliers('from_this_person_to_poi', data_dict)
showColumnOutliers('director_fees', data_dict)
showColumnOutliers('deferred_income', data_dict)
showColumnOutliers('from_poi_to_this_person', data_dict)
showColumnOutliers('long_term_incentive', data_dict)
