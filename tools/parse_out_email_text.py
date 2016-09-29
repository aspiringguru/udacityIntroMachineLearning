#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated) 
        
        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)
        
        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:
        ### remove punctuation
        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)

        ### project part 2: comment out the line below
        #words = text_string
        from nltk.stem.snowball import SnowballStemmer
        #print("available languages =", " ".join(SnowballStemmer.languages))
        #stemmer = SnowballStemmer("english")
        stemmer = SnowballStemmer("english", ignore_stopwords=True)
        #stemmer = SnowballStemmer("english")
        #print "type(stemmer)=", type(stemmer)
        #print "type(content)=", type(content)
        #print "type(text_string)=", type(text_string), "text_string=", text_string
        text_stringWords = text_string.split(" ")
        #print "type(text_stringWords)=", type(text_stringWords), "len(text_stringWords)=", len(text_stringWords)
        for myword in text_stringWords:
            myword = myword.rstrip()
            myword = myword.strip()
            #print "myword='{0}' , stemmer.stem(myword)='{1}'".format(myword, stemmer.stem(myword))
            if len(myword)>0:
                words += " "+stemmer.stem(myword)
        words = words.strip()#remove leading space.
        words = words.rstrip()
        words = words.lstrip()

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)
        #print "words=", words




    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()

