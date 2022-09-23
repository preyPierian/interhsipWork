import re
from category_obj import category_object
import Category_Utility as ca
from sql_library import sql_connector 


input_dp = sql_connector("localhost","root","root","data2")
table_input =  (input_dp.sql_fields_query("sku,item_desc,text,retailer_text","data2.tescoscrape"))
#table_input = [table_input[0:1000]]

for data in table_input :
    sku = data[0]
    item_desc = data[1]
    text = data[2]
    retailer_text = data[3]
    if (isinstance(retailer_text,str) == False) :
        retailer_text = ""
    if(isinstance(text,str) == False) :
        text = ""
    if(isinstance(item_desc,str) == False) :
        item_desc = ""
    #print(sku + item_desc)
    item_data = (ca.checkTextForCategory(item_desc,retailer_text,text,"Tesco",sku,"test"))
    if (item_data["drinkcat1"] == "Wine" ) and (((item_data["drinkcat3"] != "Rose" ) and (item_data["drinkcat3"] != "Red" ) and (item_data["drinkcat3"] != "White" ) and (item_data["drinkcat3"] != "Mulled" ))) :
        print(item_data)
        print(sku)

    
