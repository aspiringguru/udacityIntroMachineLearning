
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
        #print "incompatible type"
        salaries.append(0)
        incompatCount += 1
    else:
        salaries.append(salary)

print "incompatCount=", incompatCount
print "salaries=", salaries
print "type(salaries)=", type(salaries), "type(salaries[0])=", type(salaries[0]), "len(salaries)=", len(salaries), "len(row_names)=", len(row_names)
df = DataFrame({'name': row_names, 'salary': salaries})
#print df
print "df.shape as loaded, no cleaning."
print df.shape
print "deleting rows with Salary == 0"
df = df[df.salary!=0]
print df.shape

#result = df.sort(['salary'], ascending=[True])
result = df.sort_values(by=['salary'], ascending=[True])
#print "sorted DF = ", result
print "result.shape=", result.shape

print "top 10 salaries"
print result.tail(10)
#print "result['salary']=", result['salary']
print type(result['salary'])
print type(list(result['salary']))

plt.hist(list(result['salary']), 50, normed=1, facecolor='green', alpha=0.75)
plt.grid(True)
plt.show()

#from the result.tail above and the plot, we see an outlier 'Total' which needs to be deleted.
result = result[result.name!='TOTAL']
print "Top 10 salaries after outlier deleted."
print result.tail(10)

plt.hist(list(result['salary']), 50, normed=1, facecolor='green', alpha=0.75)
plt.grid(True)
plt.show()

#after removing the outlier 'TOTAL' we can see three people with salaries significantly higher than the rest
# but not out of range by order of magnitude.

#--------------------------------------------------------------------------------------------
#now repeat for another column
print 'checking and cleaning total_payments'
total_payments = []
for row in row_names:
    total_payment = data_dict[row]['total_payments']
    if isinstance(total_payment, basestring):
        print "incompatible type"
        total_payments.append(0)
        incompatCount += 1
    else:
        total_payments.append(total_payment)

print "incompatCount=", incompatCount
print "total_payments=", total_payments
print "type(total_payments)=", type(total_payments), "len(total_payments)=", len(total_payments), "len(row_names)=", len(row_names)

df = DataFrame({'name': row_names, 'total_payments': total_payments})
print "df.shape as loaded, no cleaning."
print df.shape
print "deleting rows with Salary == 0"
df = df[df.total_payments!=0]
print df.shape

result = df.sort_values(by=['total_payments'], ascending=[True])
#print "sorted DF = ", result
print "result.shape=", result.shape

print "top 10 total_payments"
print result.tail(10)
#print "result['salary']=", result['salary']
print type(result['total_payments'])
print type(list(result['total_payments']))

plt.hist(list(result['total_payments']), 50, normed=1, facecolor='green', alpha=0.75)
plt.grid(True)
plt.show()

#again we see 'TOTAL' is an outlier.
result = result[result.name!='TOTAL']
print "top 10 total_payments"
print result.tail(10)
plt.hist(list(result['total_payments']), 50, normed=1, facecolor='green', alpha=0.75)
plt.grid(True)
plt.show()

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

    print "top 10 salaries"
    print result.tail(10)
    # print "result['salary']=", result['salary']
    print type(result['colName'])
    print type(list(result['colName']))

    plt.hist(list(result['colName']), 50, normed=1, facecolor='green', alpha=0.75)
    plt.grid(True)
    plt.show()

showColumnOutliers('salary', data_dict)