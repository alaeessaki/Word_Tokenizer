#from nltk.tokenize import word_tokenize
#file_content = open("documents/bobo.txt" ,"r")

#tokens = word_tokenize(str(file_content.read()))

#print(tokens)
import re
import nltk
#import random
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords



#word_tokenizer funtion : it will tokenize your file and romove the special characeters
#this function can't work if you dont import nltk.tokenize from word_tokenize
#and import nltk.tokenize from RegexpTokenizer to remove special characters

def wrd_tokenize (source):
    file_content = open(source,"r")
    tokens = word_tokenize(str(file_content.read()))
    tokenizer = RegexpTokenizer(r'\w+')
    tokens =str(tokens)
    tokens = tokenizer.tokenize(tokens)
    tokens = [word.lower() for word in tokens]   
    stop_words = set(stopwords.words('english'))
    words = [w for w in tokens if not w in stop_words]
    return words
    
#wrd_tokenize("documents/bobo.txt")
wrd_tokenize("documents/bobo2.txt")

#print(wrd_tokenize("documents/bobo.txt"))

#word_classifier fucntion : it will give you most frequence words in a text, you will choose how many words you wants
#this function can't work if you don't import nltk.tokenize from 
#this funtion can't work if you don't recall the word_tokenize funtion !!!!!!!!!

def wrd_classify (source, numb):
    dct = wrd_tokenize(source)
    words = []
    for w in dct :
        words.append(w.lower())
    words = nltk.FreqDist(words)
    words = words.most_common(numb)
    return words
    #print(words)
    
#words = wrd_classify("documents/bobo.txt", 50)
words = wrd_classify("documents/bobo2.txt", 50)

def del_num(words):
    words=str(words)
    words = re.sub(r'\d+', '', words)
    words=str(words)
    return words

words = del_num(words)

def write_in_file(source, words):
    source=str(source)
    words=str(words)
    f=open(source,"w+")
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(words)
    tokens=str(tokens)
    f.write(tokens)
    f.close

write_in_file("Assets/documents/special_words.txt", words) 








    
