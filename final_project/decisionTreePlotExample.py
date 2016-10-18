#http://scikit-learn.org/stable/modules/tree.html
#not working???

from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

import pydotplus
from IPython.display import Image
dot_data = tree.export_graphviz(clf, out_file="tempxx", feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True, special_characters=True)

print "type(dot_data)=", type(dot_data)