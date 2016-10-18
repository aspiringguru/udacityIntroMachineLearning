from sklearn.datasets import load_iris
from sklearn import tree
clf = tree.DecisionTreeClassifier()
iris = load_iris()
clf = clf.fit(iris.data, iris.target)
tree.export_graphviz(clf, out_file='tree_.dot')
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf, out_file="tree__.dot")
graph = pydot.graph_from_dot_data(dot_data.getvalue())
print "========="
print "type(graph)=", type(graph)
print graph
graph.write_pdf("iris.pdf")