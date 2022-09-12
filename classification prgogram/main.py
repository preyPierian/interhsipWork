import datetime
import os
# import tesco_category_processor2 as tesco
# import amazon_profitero_category_processor2 as amazonProfitero
# import sainsbury_category_processor as sainsbury
# import morrisons_category_processor2 as morrisons
# import ocado_category_processor2 as ocado
# import waitrose_category_processor2 as waitrose
# import asda_category_processor2 as asda

import tesco_retailer_category_pull as tesco
import amazon_retailer_category_pull as amazonProfitero
import sainsbury_retailer_category_pull as sainsbury
import morrisons_retailer_category_pull as morrisons
import ocado_retailer_category_pull as ocado
import waitrose_retailer_category_pull as waitrose
import asda_retailer_category_pull as asda
import asda2_retailer_category_pull as asda2

import data_category_processor

def checkTempFolders(processing_list):
    #this script runs to check if there are any files to be processed

    #check for tesco files
    for file in os.listdir("fileUpload/Tesco"):
        #print(file)
        addFileToList(file, 1,processing_list)

    for file in os.listdir("fileUpload/Sainsbury"):
        addFileToList(file, 3, processing_list)

    for file in os.listdir("fileUpload/Morrisons"):
        addFileToList(file, 4, processing_list)

    for file in os.listdir("fileUpload/Ocado"):
        addFileToList(file, 5, processing_list)

    for file in os.listdir("fileUpload/ASDA"):
        addFileToList(file, 6, processing_list)

    for file in os.listdir("fileUpload/Waitrose"):
        addFileToList(file, 8, processing_list)

    for file in os.listdir("fileUpload/Profitero"):
        #print(file)
        addFileToList(file, 2,processing_list)

    for file in os.listdir("fileUpload/ASDA2"):
        #print(file)
        addFileToList(file, 10,processing_list)

def addFileToList(file_name, rule, processing_list):

    processing_list.append(file_data)
file_data = {"file":file_name, "rule":rule, "status": "unprocessed"}
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #Initiate list
    processing_list = []
    #Initiate data processor

    data_service = data_category_processor.DataCategoryProcessor()

    #Fill list with files in temp folder
    checkTempFolders(processing_list)

    #process files in list
    for list_item_index in range(len(processing_list)):
        list_item = processing_list[list_item_index]
        if list_item["status"] == "unprocessed":
            print("processing file " + list_item["file"])
            # if(list_item["rule"] == 1):   #READY
            #     result = tesco.processFile(list_item, data_service)
            #     print("")
            #     print(result)
            #     data_service.recordLog("completed Tesco Category pull file " + list_item["file"] + " With Result " + str(result))
            #     processing_list[list_item_index]["status"] = result["Status"]
            #     processing_list[list_item_index]["result"] = result
            #
            # if (list_item["rule"] == 2):
            #     result = amazonProfitero.processFile(list_item, data_service)
            #     print("")
            #     print(result)
            #     data_service.recordLog(
            #         "completed Amazon Category pull file " + list_item["file"] + " With Result " + str(result))
            #     processing_list[list_item_index]["status"] = result["Status"]
            #     processing_list[list_item_index]["result"] = result
            #
            # if (list_item["rule"] == 3):  #SORT OF
            #     result = sainsbury.processFile(list_item, data_service)
            #     print("")
            #     print(result)
            #     data_service.recordLog(
            #         "completed Sainsbury Category pull file " + list_item["file"] + " With Result " + str(result))
            #     processing_list[list_item_index]["status"] = result["Status"]
            #     processing_list[list_item_index]["result"] = result
            #
            # if (list_item["rule"] == 4): #READY
            #     result = morrisons.processFile(list_item, data_service)
            #     print("")
            #     print(result)
            #     data_service.recordLog(
            #         "completed Morrisons Category pull file " + list_item["file"] + " With Result " + str(result))
            #     processing_list[list_item_index]["status"] = result["Status"]
            #     processing_list[list_item_index]["result"] = result
            #
            # if (list_item["rule"] == 5): #READY
            #     result = ocado.processFile(list_item, data_service)
            #     print("")
            #     print(result)
            #     data_service.recordLog(
            #         "completed Ocado Category pull file " + list_item["file"] + " With Result " + str(result))
            #     processing_list[list_item_index]["status"] = result["Status"]
            #     processing_list[list_item_index]["result"] = result
            # #
            # if (list_item["rule"] == 6):  #READY
            #     result = asda.processValueFile(list_item, data_service)
            #     print("")
            #     print(result)
            #     data_service.recordLog(
            #         "completed ASDA Category pull file " + list_item["file"] + " With Result " + str(result))
            #     processing_list[list_item_index]["status"] = result["Status"]
            #     processing_list[list_item_index]["result"] = result
            #
            # if (list_item["rule"] == 8):  #SORT OF
            #     result = waitrose.processFile(list_item, data_service)
            #     print("")
            #     print(result)
            #     data_service.recordLog(
            #         "completed Waitrose Category pull file " + list_item["file"] + " With Result " + str(result))
            #     processing_list[list_item_index]["status"] = result["Status"]
            #     processing_list[list_item_index]["result"] = result

            if (list_item["rule"] == 10):  #SORT OF
                result = asda2.processFile(list_item, data_service)
                print("")
                print(result)
                data_service.recordLog(
                    "completed asda2 Category pull file " + list_item["file"] + " With Result " + str(result))
                processing_list[list_item_index]["status"] = result["Status"]
                processing_list[list_item_index]["result"] = result

    # print("")
    # print(processing_list)
    # print(data_service.tesco_data.head())
    #
    # #SAVE DATA TABLES TO CSV
    # dt = datetime.datetime.now()    # current date and time
    # dt_string = dt.strftime("%Hh-%Mm-%Ss_%d-%m-%Y")
    # cwd = os.getcwd()
    # save_dir = cwd+"/export_"+dt_string
    # os.mkdir(save_dir)
    # data_service.sales_data.to_csv(save_dir+"/sales_data.csv")
    # data_service.unit_data.to_csv(save_dir+"/unit_data.csv")
    # data_service.asp_data.to_csv(save_dir+"/asp_data.csv")
