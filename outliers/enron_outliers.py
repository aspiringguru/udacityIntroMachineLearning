#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
print "type(data_dict)=", type(data_dict)
print "data_dict.keys=", list(data_dict.keys())
print "len(list(data_dict.keys()))=", len(list(data_dict.keys()))
print data_dict['METTS MARK']
print data_dict['METTS MARK'].keys()
print type(data_dict['METTS MARK']['salary'])
print type(data_dict['METTS MARK']['bonus'])
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.title("before outlier removed")
matplotlib.pyplot.show()

salaries = []
bonuses = []
for name in list(data_dict.keys()):
    salary = data_dict[name]['salary']
    if isinstance(salary, basestring):
        salaries.append(-1)
    else:
        salaries.append(data_dict[name]['salary'])

    bonus = data_dict[name]['bonus']
    if isinstance(bonus, basestring):
        bonuses.append(-1)
    else:
        bonuses.append(data_dict[name]['bonus'])

max_salaryIndex = salaries.index(max(salaries))
print "index of max salary = ", max_salaryIndex
maxBonusIndex = bonuses.index(max(bonuses))
print "index of max bonus = ", maxBonusIndex
maxBonusName = list(data_dict.keys())[bonuses.index(max(bonuses))]

print "name @ index of max bonus = ", maxBonusName
print data_dict[maxBonusName]

data_dict.pop(maxBonusName, 0)


data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.title("after outlier removed")
matplotlib.pyplot.show()


# Identifying Two More Outliers
"""
We would argue that there's 4 more outliers to investigate let's look at a couple of them.
Two people made bonuses of at least 5 million dollars, and a salary of over 1 million dollars
in other words, they made out like bandits. What are the names associated with those points?
"""
print "\nafter outlier removed\n"
print "last two bonuses = ", sorted(bonuses)[-2:]

max_salaryIndex = salaries.index(max(salaries))
print "index of max salary = ", max_salaryIndex
maxBonusIndex = bonuses.index(max(bonuses))
print "index of max bonus = ", maxBonusIndex
maxBonusName = list(data_dict.keys())[bonuses.index(max(bonuses))]

print "name @ index of max bonus = ", maxBonusName
print data_dict[maxBonusName]

secondMaxBonus = sorted(bonuses)[-2]
secondMaxBonusName = list(data_dict.keys())[bonuses.index(secondMaxBonus)]
print "secondMaxBonusName=", secondMaxBonusName, "secondMaxBonus=", secondMaxBonus

secondMaxBonus = sorted(bonuses)[-3]
secondMaxBonusName = list(data_dict.keys())[bonuses.index(secondMaxBonus)]
print "3rd max bonus=", secondMaxBonusName, "secondMaxBonus=", secondMaxBonus

print "LAY KENNETH L=", data_dict['LAY KENNETH L']
print "LAVORATO JOHN J=", data_dict['LAVORATO JOHN J']


from pprint import pprint
outliers = []
salaries2 = []
bonuses2 = []
for key in data_dict:
    val = data_dict[key]['salary']
    bonus = data_dict[key]['bonus']
    if val != 'NaN':
        outliers.append((key,int(val)))
        salaries2.append(val)
    if bonus != 'NaN':
        bonuses2.append(bonus)

salaries2 = sorted(salaries2)
bonuses2 = sorted(bonuses2)
print type(outliers)
print type(outliers[-1])
print type(salaries2)
print "salaries2[-2:]=", salaries2[-2:]
#salaries2[-2:]= [1072321, 1111258]
print "max salaries = ", list(data_dict.keys())[salaries.index(salaries2[-2])]
#max salaries =  LAY KENNETH L
print "2nd max salaries = ", list(data_dict.keys())[salaries.index(salaries2[-1])]
#2nd max salaries =  SKILLING JEFFREY K



print type(bonuses)
print "bonuses2[-2:]=", bonuses2[-2:]
#bonuses2[-2:]= [7000000, 8000000]
print list(data_dict.keys())[bonuses.index(bonuses2[-2])]
#LAY KENNETH L
print list(data_dict.keys())[bonuses.index(bonuses2[-1])]
#LAVORATO JOHN J


print "two max salaries from pprint"
pprint(sorted(outliers,key=lambda x:x[1],reverse=True)[:2])
#[('SKILLING JEFFREY K', 1111258), ('LAY KENNETH L', 1072321)]

