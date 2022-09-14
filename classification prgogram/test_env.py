import re
from category_obj import category_object
import Category_Utility as ca
from sql_library import sql_connector 


input_dp = sql_connector("localhost","root","root","data2")

table_input =  (input_dp.sql_fields_query("sku,item_desc,text,retailer_text","data2.tescoscrape"))
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
    print(ca.checkTextForCategory(item_desc,retailer_text,text,"Tesco",sku,"test"))
