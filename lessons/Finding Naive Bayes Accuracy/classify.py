def NBAccuracy(features_train, labels_train, features_test, labels_test):
    """ compute the accuracy of your Naive Bayes classifier """
    ### import the sklearn module for GaussianNB
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score

    ### create classifier
    clf = GaussianNB() #TODO

    ### fit the classifier on the training features and labels
    clf.fit(features_train, labels_train)#TODO

    ### use the trained classifier to predict labels for the test features
    pred = clf.predict([[-0.8, -1]])#TODO


    ### calculate and return the accuracy on the test data
    ### this is slightly different than the example, 
    ### where we just print the accuracy
    ### you might need to import an sklearn module
    accuracy = clf.accuracy_score(features_train, labels_train)#TODO
    return accuracy

    """
    http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
    sklearn.metrics.accuracy_score(y_true, y_pred, normalize=True, sample_weight=None)

    """