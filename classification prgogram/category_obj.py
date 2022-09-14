import re
import Category_Utility as ca

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
    
    def update_category(self, category_num, category_name, search_query ) :
        pos = self.find_pos(search_query)
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

    
    def find_pos(self,search_query) :
        combined_words = ""
        if len(search_query) == 1:
            combined_words = ca.joinkeywordslean(search_query)
        else :
            combined_words = ca.joinkeywordsfulllean(search_query)
        return(re.search(combined_words, self.str, re.IGNORECASE).start())