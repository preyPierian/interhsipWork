import re
import Category_Utility

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
        pos = re.search(joinkeywordsfulllean(vodka), str, re.IGNORECASE).start()
        re.search(joinkeywords(one_varietal), str, re.IGNORECASE).start()
        match category_num :
            case 1 :
                self.drinkCat1 = category_name
            case 2 :
                self.drinkCat2 = category_name 
            case 3 :
                self.drinkCat3 = category_name
            case 4 :
                self.drinkCat4 = category_name
            case _:
                raise Exception("Invalid category")
    
    def find_pos(self,search_query) :
        if len(search_query) == 1:
            
