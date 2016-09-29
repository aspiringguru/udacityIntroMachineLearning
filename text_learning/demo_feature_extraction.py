"""
http://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction
"""

from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)
print vectorizer

corpus = ['This is the first document.', 'This is the second second document.', 'And the third one.', 'Is this the first document?',]
X = vectorizer.fit_transform(corpus)
print "type(X)=", type(X)
print "X=\n", X


analyze = vectorizer.build_analyzer()
print analyze("This is a text document to analyze.") == (['this', 'is', 'text', 'document', 'to', 'analyze'])
#returns True

print vectorizer.get_feature_names() == (['and', 'document', 'first', 'is', 'one','second', 'the', 'third', 'this'])
#returns True

print  X.toarray()
#[[0 1 1 1 0 0 1 0 1]
# [0 1 0 1 0 2 1 0 1]
# [1 0 0 0 1 0 1 1 0]
# [0 1 1 1 0 0 1 0 1]]

print vectorizer.vocabulary_.get('document')

