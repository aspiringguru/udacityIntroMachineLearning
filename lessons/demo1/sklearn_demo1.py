import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

clf = GaussianNB()
print ("type(clf)=", type(clf))
clf.fit(X, Y)
print ("after clf.fit, type(clf)=", type(clf))
print ("clf.score(X, Y)=", clf.score(X, Y) )
print("predict [-0.8, -1] = ", clf.predict([[-0.8, -1]]))




"""
clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
print ("after clf_pf.partial_fit, type(clf_pf)=", type(clf_pf))
print(clf_pf.predict([[-0.8, -1]]))
print ("clf_pf.score(X, Y)=", clf_pf.score(X, Y) )

clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
print ("after clf_pf.partial_fit with np.unique(Y), type(clf_pf)=", type(clf_pf))
print(clf_pf.predict([[-0.8, -1]]))
print ("clf_pf.score(X, Y)=", clf_pf.score(X, Y) )

"""