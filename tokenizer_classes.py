import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


class tokenizer :
    def __init__(self, import_source):
        self.import_source = import_source
    
    #wrd_tokenizer divise the text with a source given and transform it to words
        
    def wrd_tokenizer (self, source): 
        file_content = open(source,"r")
        tokens = word_tokenize(str(file_content.read()))
        tokenizer = RegexpTokenizer(r'\w+')
        tokens = str(tokens)
        tokens = tokenizer.tokenize(tokens)
        tokens = [word.lower() for word in tokens]   
        stop_words = set(stopwords.words('english'))
        words = [w for w in tokens if not w in stop_words]
        self.tokens = words
    
    #wrd_classifier classify the words that were tokenizied depends to how many word you want
    #NB: to use this methode you need to call the wrd tokenizer first
        
    def wrd_classifier (self, tokens, numb):
        dtc = tokens
        words = []
        for w in dtc:
            words.append(w)
        words = nltk.FreqDist(words)
        words = words.most_common(numb)
        self.top_words = words

    #del_num delete all numbers from your text
        
    def del_num(self, top_words):
        dtc = str(top_words)
        dtc = re.sub(r'\d+', '', dtc)
        tokenizer = RegexpTokenizer(r'\w+')
        dtc = tokenizer.tokenize(dtc)
        self.wn_words = dtc
        
    #write_in_file it export your file to a source given
        
    def write_in_file(self, source, wn_words):
        source=str(source)
        dtc = str(wn_words)
        f=open(source,"w+")
        f.write(dtc)
        f.close   
   












#####exemple#####
        
    
tokenize1 = tokenizer("../Assets/documents/bobo.txt")
tokenize1.wrd_tokenizer("../Assets/documents/bobo.txt")
tokens = tokenize1.tokens
print(tokens)
tokenize1.wrd_classifier(tokens, 16)

top_words = tokenize1.top_words
print(top_words)
#tokenize1.del_num(top_words)

#words = tokenize1.wn_words
#tokenize1.write_in_file("src.txt", words)



#print(tokenize1.wn_words)
