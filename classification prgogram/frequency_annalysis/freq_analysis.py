import re

class anyalsis :
    def __init__(self,word,first_occur,frequency) :
        self.word = word
        self.first_occur = first_occur
        self.frequency = frequency

def freq_annalysis(keywords,text) :
    count = 1
    arr_text = (text.lower()).split(" ")
    set_text = set(arr_text)
    for current_word in set_text :
        if current_word in  keywords :
            print(current_word)
            feq = arr_text.count(current_word)
            first_occur = text.find(current_word)
            print(str(feq) + " "+  str(first_occur))
        #filtered_text = filter(lambda word: word != current_word, text )
        #text = list(filtered_text)
        #print(text)

freq_annalysis(["and","lol"],"lol it funny and lol i love it")


