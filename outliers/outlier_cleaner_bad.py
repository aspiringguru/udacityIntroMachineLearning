#!/usr/bin/python


from __future__ import print_function


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).

        It takes three arguments: predictions is a list of predicted targets that come from your regression,
        ages is the list of ages in the training set,
        and net_worths is the actual value of the net worths in the training set.

         return a list called cleaned_data that has only 81 elements in it,
         which are the 81 training points where the predictions
         and the actual values (net_worths) have the smallest errors (90 * 0.9 = 81)
    """
    
    cleaned_data = []

    ### your code goes here
    print ("\noutlier_cleaner---------")
    print ("type(predictions)=", type(predictions))
    print ("type (ages)=", type (ages))
    print ("type(net_worths)=", type(net_worths))
    print ("predictions.shape=", predictions.shape)
    print ("ages.shape=", ages.shape)
    print ("net_worths.shape=", net_worths.shape)
    print ("predictions.tolist()=", predictions.tolist())
    print ("ages.tolist()=", ages.tolist())
    print ("net_worths.tolist()=", net_worths.tolist())
    from itertools import chain
    predictions = list(chain.from_iterable(predictions))
    ages = list(chain.from_iterable(ages))
    net_worths = list(chain.from_iterable(net_worths))
    print ("len(predictions) =", len(predictions), type(predictions), predictions)
    print ("len(ages) =", len(ages), type(ages), ages)
    print ("len(net_worths) =", len(net_worths), type(net_worths), net_worths)

    for i in range(len(predictions)):
        cleaned_data.append(abs(predictions[i]-net_worths[i]))
    print ("cleaned_data=", cleaned_data)
    cleaned_data = sorted(cleaned_data, key=int)
    print ("sorted cleaned_data=", cleaned_data)
    print ("11. type(cleaned_data)=", type(cleaned_data))
    """
    try:
        cleaned_data = np.asarray(cleaned_data)#error?
    except:
        print ("error trapped")
        e = sys.exc_info()[0]
        print ("------")
        print ("e=", e)
        print ("error=", Error)
    """
    #cleaned_data = np.asarray(cleaned_data)
    print('22. type(cleaned_data)=', type(cleaned_data))

    return cleaned_data

