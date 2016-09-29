#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
#sys.path.append( "..\tools\" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.

    https://www.udacity.com/course/viewer#!/c-ud120/l-2892378590/e-3011238671/m-2998398623
    refer Lesson 10 Text Learning : Clean Away "Signature Words"
"""


from_sara  = open("from_sara.txt", "r").read().splitlines()
from_chris = open("from_chris.txt", "r").read().splitlines()

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    #loads lines from files for sara then chris.
    for path in from_person:
        path = path.rstrip()#delete the newline character at end of string.
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        #temp_counter += 1#
        if temp_counter < 200:
            #print "path in from_person = ", path
            pathElements = path.split("/")
            #print "pathElements ", pathElements
            temp = ""
            for element in pathElements:
                temp = os.path.join(temp, element)
            #print "temp=", temp
            path = "..\\"+temp[:-1]+"_"#removes '.' at end. seems to be hangover from linux to windows.
            #print "path=", path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            stemmedText = parseOutText(email)
            #print "type(stemmedText)=", type(stemmedText)
            #print "stemmedText=", stemmedText



            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            wordsToRemove = ["sara", "shackleton", "chris", "germani"]
            stemmedText = stemmedText.lower()
            for word in wordsToRemove:
                stemmedText = stemmedText.replace(word, "")
            #print "stemmedText after stripping words = ", stemmedText

            #NB: these two lines are a kludge fix for errors introduced when reading files
            #Need to review how files are read.
            stemmedText = stemmedText.replace("\n", " ")
            stemmedText = stemmedText.replace("  ", " ")
            ### append the text to word_data
            word_data.append(stemmedText)
            #print "word_data=", word_data


            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            from_data.append(0 if name == "sara" else 1)


            email.close()

print "emails processed"
# file close is not required when open(blah).read().splitlines() is used.
#from_sara.close()
#from_chris.close()

print "---------------------------------------------"
print "word_data[152]=", repr(word_data[152])
print "---------------------------------------------"

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )





### in Part 4, do TfIdf vectorization here

from nltk.corpus import stopwords
sw = stopwords.words("english")

print "type(sw)=", type(sw)
print "type(sw[0])=", type(sw[0])
print "len(sw)=", len(sw)
print "sw=", sw
sw = sw + wordsToRemove
print "after adding 'wordsToRemove' len(sw)=", len(sw)

#Remove english stopwords.


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words = sw, lowercase=True)
#vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)

#NB lowercase : boolean, default True

vectorizer.fit_transform(word_data)
# bag_words = vectorizer.transform(word_data)

# Get how many unique words there are in the emails
print "type(vectorizer.get_feature_names())=", type(vectorizer.get_feature_names())
#list
#for i in range(10):
#    print "type(vectorizer.get_feature_names()[{}])=".format(i), type(vectorizer.get_feature_names()[i])
#    print "vectorizer.get_feature_names()[{}])=".format(i), vectorizer.get_feature_names()[i]
#NB this showed the elements of vectorizer.get_feature_names() are not strings.

print "len(vectorizer.get_feature_names())=", len(vectorizer.get_feature_names())
#incorrect answers so far.
#41976
#42117
#44993
#41973

#How many different words are there?
print "size of set = ", len(set(vectorizer.get_feature_names()))
#size of set =  42117

# Word number 34597
print "word[34597]=", vectorizer.get_feature_names()[34597]

#check if element matches elements of wordsToRemove = ["sara", "shackleton", "chris", "germani"]


from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer, TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(word_data)
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(X)
print "BBBBB", len(vectorizer.get_feature_names())


