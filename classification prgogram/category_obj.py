import re
#import Category_Utility as ca

class category_object : 
    def __init__(self,str) :
        self.drinkCat1 = ""
        self.cat_1_pos = 9999
        self.drinkCat2 = ""
        self.cat_2_pos = 9999
        self.drinkCat3 = ""
        self.cat_3_pos = 9999
        self.drinkCat4 = ""
        self.cat_4_pos = 9999
        self.flavoured =  0
        self.rtd =  0
        self.str = " "+str+" "

    
    def joinkeywords(arr):
        full_pattern = ""
        for word_index in range(len(arr)):
            if word_index > 0:
                full_pattern = full_pattern + "|"
            full_pattern = full_pattern + " " + arr[word_index] + " "#|"+arr[word_index]+" "

        return full_pattern

    def joinkeywordslean(self,arr):
        full_pattern = ""
        for word_index in range(len(arr)):
            if word_index > 0:
                full_pattern = full_pattern + "|"
            full_pattern = full_pattern + " " + arr[word_index] + "|"+arr[word_index]+" "

        return full_pattern

    def joinkeywordsfulllean(self,arr):
        full_pattern = ""
        for word_index in range(len(arr)):
            if word_index > 0:
                full_pattern = full_pattern + "|"
            full_pattern = full_pattern + arr[word_index]

        return full_pattern
    
    def update_category(self, category_num, category_name, search_query ) :
        pos = self.first_pos(search_query)
        match category_num :
            case 1 :
                self.drinkCat1 = category_name
                self.cat_1_pos =  pos 
            case 2 :
                self.drinkCat2 = category_name 
                self.cat_2_pos = pos
            case 3 :
                self.drinkCat3 = category_name
                self.cat_3_pos = pos
            case 4 :
                self.drinkCat4 = category_name
                self.cat_4_pos = pos
            case _:
                raise Exception("Invalid category")

    def update_flavour(self,is_flavoured) :
        if is_flavoured == True : 
            self.flavoured = 1
        else :
            self.flavoured = 0
    
    
    def update_rtd(self,is_rtd) :
        if is_rtd == True : 
            self.flavoured = 1
        else :
            self.flavoured = 0

    def combined_words(self,search_query) :
        combined_words = ""
        if len(search_query) == 1:
            combined_words = self.joinkeywordslean(search_query)
        else :
            combined_words = self.joinkeywordsfulllean(search_query)
        return(combined_words)


    def first_pos(self,query) :
        return(re.search(self.combined_words(query), self.str, re.IGNORECASE).start())
    
    def exsits(self,query) :
        if re.search(self.combined_words(query), self.str, re.IGNORECASE) != None :
            if (len(re.findall(self.combined_words(query), self.str, re.IGNORECASE))>0):
                return(True)
            else:
                return False
        else :
            return False