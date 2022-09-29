import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd  
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize

class analysis :
    def __init__(self,word,first_occur,frequency) :
        self.word = word
        self.first_occur = first_occur
        self.frequency = frequency

def freq_analysis(keywords,text) :
    dict = {'keywords':[],'freq':[],'first_occurance':[]}
    #count = 1
    stop_words = (stopwords.words('english'))

    arr_text = (text.lower()).split(" ")
    arr_text = [w for w in arr_text if not w.lower() in stop_words]
    print(arr_text)

    set_text = set((arr_text))
    for current_word in set_text :
        if current_word in  keywords :
            print(current_word)
            feq = arr_text.count(current_word)
            first_occur = text.find(current_word)
            print(str(feq) + " "+  str(first_occur))
            dict["keywords"].append(current_word)
            dict["freq"].append(arr_text.count(current_word))
            dict["first_occurance"].append(text.find(current_word))
    print(dict)
    print( pd.DataFrame(dict))

freq_analysis(["weather","nice", "really"],"The weather is looking really nice today. I hope it stays nice !")