from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.metrics import accuracy_score
y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]

clf = GaussianNB()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

print "accuracy_score=", accuracy_score(y_true, y_pred) 