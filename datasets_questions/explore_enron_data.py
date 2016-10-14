#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from __future__ import division
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "type(enron_data)=", type(enron_data)
print "len(enron_data)=", len(enron_data)
print "len(enron_data.keys())=", len(enron_data.keys())
print "enron_data.keys()=", enron_data.keys()
print len(enron_data['METTS MARK'])
#for key in enron_data.keys():
#    print len(enron_data[key])
#NB: all have 21 records.
print type(enron_data['METTS MARK'])
print "enron_data['METTS MARK'].keys()=", enron_data['METTS MARK'].keys()
print enron_data['METTS MARK']['poi']
print type(enron_data['METTS MARK']['poi'])

#How Many POIs Exist?
countPOI = 0
for key in enron_data.keys():
    if enron_data[key]['poi']:
        countPOI += 1
print "countPOI =", countPOI

#What is the total value of the stock belonging to James Prentice?
print "---------"
name = 'Prentice James'
for key in enron_data.keys():
    #print type(key), key
    if name.lower() in key.lower():
        print "match found \n\n\n\n"
        print 'total_stock_value for ', key, ' =', enron_data[key]['total_stock_value']
        break


"""
print "---------"
name = 'Colwell Wesley'
for key in enron_data.keys():
    print type(key), key
    if name.lower() in key.lower():
        print "match found \n\n\n\n"
        print 'from_poi_to_this_person=', enron_data[key]['from_poi_to_this_person']
        print 'from_this_person_to_poi=', enron_data[key]['from_this_person_to_poi']
        break
"""

#What is the value of stock options exercised by Jeffrey K Skilling?
"""
print "---------"
name = 'Skilling Jeffrey'
for key in enron_data.keys():
    print type(key), key
    if name.lower() in key.lower():
        print "match found \n\n\n\n"
        print 'exercised_stock_options=', enron_data[key]['exercised_stock_options']
        break
"""

"""
#Follow the Money
#Of these three individuals (Lay, Skilling and Fastow),
#Jeffrey Skilling, Ken Lay, Andrew Fastow
# who took home the most money (largest value of "total_payments" feature)?
#How much money did that person get?
def getInfoByName(name, param):
    for key in enron_data.keys():
        #print type(key), key
        if name.lower() in key.lower():
            print "match found \n\n\n\n"
            print param, ' = ', enron_data[key][param]
            return enron_data[key][param]

results = []
results.append(getInfoByName("Skilling Jeffrey", "total_payments"))
results.append(getInfoByName("Lay Ken", "total_payments"))
results.append(getInfoByName("Fastow Andrew", "total_payments"))
print results
"""

"""
#Unfilled Features
count = 0
for key in enron_data.keys():
 print type(key), key
 print enron_data[key]
 count += 1
 if count>5: break
"""


"""
#Dealing with Unfilled Features
#How many folks in this dataset have a quantified salary? What about a known email address?
#'salary'  'email_address'
print "-------------------aaa"
import math
count = 0
countSalaryNotNAN = 0
countEmailNotNAN = 0
for key in enron_data.keys():
    #print type(enron_data[key]), enron_data[key]
    #print type(enron_data[key]['salary']), type(enron_data[key]['email_address'])
    if not isinstance(enron_data[key]['salary'], basestring):
        countSalaryNotNAN += 1
    #if not math.isnan(enron_data[key]['email_address']):
    #if isinstance(enron_data[key]['email_address'], basestring):
    if not enron_data[key]['email_address'] == "NaN":
        countEmailNotNAN += 1
        #print enron_data[key]['email_address']

    count += 1
    #if count > 5: break

print "countSalaryNotNAN =", countSalaryNotNAN
print "countEmailNotNAN =", countEmailNotNAN
print "count = ", count
"""


"""
#Missing POIs 1 (optional)
#How many people in the E+F dataset (as it currently exists) have "NaN" for their total payments?
# What percentage of people in the dataset as a whole is this?
count = 0
for key in enron_data.keys():
    #'total_payments'
    if enron_data[key]['total_payments'] =="NaN":
        print type(enron_data[key]['total_payments']), enron_data[key]['total_payments']
        count += 1
print "No of 'total_payments' with value 'NaN' is ", count
numKeys = len(list(enron_data.keys()))
print "numKeys = ", numKeys
print count/numKeys * 100
"""

"""
#Missing POIs 2 (optional)
#How many POIs in the E+F dataset have "NaN" for their total payments?
# What percentage of POI's as a whole is this?
count = 0
for key in enron_data.keys():
    #'total_payments'
    if enron_data[key]['total_payments'] =="NaN" and enron_data[key]['poi']:
        count += 1
print "total payments are 'NaN' and POI = ", count
"""

"""
#Missing POIs 3 (optional)
#If a machine learning algorithm were to use total_payments as a feature,
# would you expect it to associate a 'NaN' value with POIs or non-POIs?
countTotalPaymentNAN = 0
countPOI = 0
countTotalPaymentNAN_POI = 0
countPOI_TotalPaymentNAN = 0
for key in enron_data.keys():
    if enron_data[key]['total_payments'] == "NaN":
        print "'total_payments'='NaN', ", key, enron_data[key]['poi'], enron_data[key]['total_payments']
        countTotalPaymentNAN += 1
        if enron_data[key]['poi']:
            countTotalPaymentNAN_POI += 1
print "TotalPayment is NAN=", countTotalPaymentNAN, ", TotalPayment is NAN & POI = ", countTotalPaymentNAN_POI

for key in enron_data.keys():
    if enron_data[key]['poi']:
        print "poi=True, ", key, enron_data[key]['poi'], enron_data[key]['total_payments']
        countPOI += 1
        if enron_data[key]['total_payments'] == "NaN":
            countPOI_TotalPaymentNAN += 1
print "No if POI =", countPOI, ", is POI & TotalPayment is NAN = ",countPOI_TotalPaymentNAN


#results,
# TotalPayment is NAN= 21 , TotalPayment is NAN & POI =  0
# No if POI = 18 , is POI & TotalPayment is NAN =  0
# ie zero overlap between TotalPayment is NAN & POI is True.

print len(enron_data.keys())

"""