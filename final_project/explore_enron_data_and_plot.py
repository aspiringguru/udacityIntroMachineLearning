import pickle
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "type(enron_data)=", type(enron_data)
print "len(enron_data)=", len(enron_data)
print "len(enron_data.keys())=", len(enron_data.keys())
print "enron_data.keys()=", enron_data.keys()
print len(enron_data['METTS MARK'])
print enron_data['METTS MARK'].keys()
print type(enron_data['METTS MARK']['salary']), enron_data['METTS MARK']['salary']

#delete key from enron data where analysis shows it is an outlier.
del enron_data['TOTAL']
del enron_data['LAY KENNETH L']
del enron_data['WHITE JR THOMAS E']
#'Total' is not referring to an individual.



def plotParam(enron_data, param):
    poiParam = []
    maxPoiParam = 0
    personMaxPoiParam = ""
    nonPoiParam = []
    maxNonPoiParam = 0
    personMaxNonPoiParam = ""
    for person in enron_data.keys():
        # print type(person), person
        # print type(enron_data[person]['poi']), enron_data[person]['poi'], type(enron_data[person]['salary']), 'salary=', enron_data[person]['salary']
        personsParam = enron_data[person][param]
        if not isinstance(personsParam, basestring):
            if enron_data[person]['poi']:
                if personsParam > maxPoiParam:
                    print param, " of ", person, " is ",personsParam, "largest POI ", param, " value to date"
                    maxPoiParam = personsParam
                    personMaxPoiParam = person
                poiParam.append(float(personsParam))
            else:
                if personsParam > maxNonPoiParam:
                    # print "salary of ", person, " is ",personsSalary, "largest non POI salary to date"
                    maxNonPoiParam = personsParam
                    personMaxNonPoiParam = person
                nonPoiParam.append(float(personsParam))

    print "len(poiParam)=", len(poiParam)
    if len(poiParam)>0: print "max(poi"+param, ")=", max(poiParam)
    print "maxPoi", param, "=", maxPoiParam, "person = ", personMaxPoiParam
    print "max(nonPoi",param,")=", max(nonPoiParam), "maxNonPoiParam=", maxNonPoiParam, "person = ", personMaxNonPoiParam
    print len(enron_data.keys())

    import numpy as np
    import matplotlib.mlab as mlab
    import matplotlib.pyplot as plt

    plt.hist(nonPoiParam, label='nonPOI')
    plt.hist(poiParam, label='POI')

    plt.xlabel(param)
    plt.ylabel('#Count')
    plt.title("Enron data, "+param+" levels POI vs Non POI")
    plt.grid(True)
    plt.legend(loc='upper right')
    plt.show()

"""
plotParam(enron_data, "salary")
plotParam(enron_data, "total_payments")
plotParam(enron_data, "exercised_stock_options")
plotParam(enron_data, "bonus")
plotParam(enron_data, "restricted_stock")
plotParam(enron_data, "total_stock_value")
plotParam(enron_data, "expenses")
plotParam(enron_data, "long_term_incentive")
"""
plotParam(enron_data, "director_fees")
#plotParam(enron_data, "loan_advances")
