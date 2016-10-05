"""
simple example from
http://scikit-learn.org/stable/modules/tree.html
"""

from sklearn import tree
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

print (clf.predict([[2., 2.]]))