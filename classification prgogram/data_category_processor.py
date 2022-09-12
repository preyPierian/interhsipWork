import datetime
import pandas as pd
import mysql.connector

class DataCategoryProcessor:


    mydb = mysql.connector
    def __init__(self):
        self.mydb = mysql.connector.connect(host="localhost", user="suprim", password="suprimpassword", database="data2")
        print("DB SETUP")
        print(self.mydb)

        self.mycursor = self.mydb.cursor()

    def getSuppliers(self):
        sql = "SELECT supplier FROM suppliers"

        try:
            self.mycursor.execute(sql)
            suppliers = self.mycursor.fetchall()
            return suppliers
        except Exception as e:
            print("failed to write to logs table with: ")
            print(e.__str__())
            return []

    def getBrands(self):
        sql = "SELECT brand, supplier FROM brandsupplier"

        try:
            self.mycursor.execute(sql)
            brands = self.mycursor.fetchall()
            return brands
        except Exception as e:
            print("failed to write to logs table with: ")
            print(e.__str__())
            return []

    def recordLog(self, text):
        datetime_now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S.000")
        sql = "INSERT INTO logs (dt, log_text) VALUES (%s, %s)"
        val = (datetime_now, text)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to logs table with: ")
            print(e.__str__())

    def retailerScrapeSupplier(self, supplier):
        # print("storing sales data")
        datetime_now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S.000")
        sql = "INSERT IGNORE INTO suppliers (supplier, upload_timestamp) VALUES (%s, %s)"
        val = [supplier, datetime_now]
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def retailerScrapeBrand(self, brand):
        # print("storing sales data")
        datetime_now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S.000")
        sql = "INSERT IGNORE INTO brandsupplier (brand, upload_timestamp) VALUES (%s, %s)"
        val = [brand, datetime_now]
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def retailerScrapeBrandSupplier(self, brand, supplier):
        # print("storing sales data")
        datetime_now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S.000")
        sql = "REPLACE INTO brandsupplier (brand, supplier, upload_timestamp) VALUES (%s, %s, %s)"
        val = [brand, supplier, datetime_now]
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()


        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())


    # def CheckForCategoryOverwrite(self,SKU, Retailer, column):
    #
    #     sql = "UPDATE " + retailerstring + "scrape SET " + column + " = %s WHERE sku = %s"
    #     val = (text, SKU)


    def retailerScrapeStore(self, SKU, Retailer, text, column):
        # print("storing sales data")
        self.retailerScapeInsertSKU(SKU, Retailer)
        retailerstring = Retailer.lower()

        sql = "UPDATE " + retailerstring + "scrape SET " + column + " = %s WHERE sku = %s"
        val = (text, SKU)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def retailerScapeInsertSKU(self, SKU, Retailer):
        retailerstring = Retailer.lower()
        sql = "INSERT IGNORE INTO " + retailerstring + "scrape (sku) VALUES (%s)"
        val = [SKU]
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def insertSKU(self,SKU, Retailer):
        retailerstring = Retailer.lower()
        sql = "INSERT IGNORE INTO "+retailerstring+"category2 (sku) VALUES (%s)"
        val = [SKU]
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def storeCategoryData(self, SKU, Retailer, value, category):
        # print("storing sales data")
        self.insertSKU(SKU, Retailer)
        retailerstring = Retailer.lower()

        sql = "UPDATE " + retailerstring + "category2 SET "+category+" = %s WHERE sku = %s"
        val = (value, SKU)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())
            print("and value " + str(value) + " for sku: " + str(SKU))

    def storeManufacturerData(self, SKU, Retailer, Value):
        #print("storing sales data")
        self.insertSKU(SKU, Retailer)
        retailerstring = Retailer.lower()

        sql = "UPDATE "+retailerstring+"category2 SET manufacturer = %s WHERE sku = %s"
        val = (Value, SKU)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def storeitemDescription(self, SKU, Retailer, Value):
        self.insertSKU(SKU, Retailer)
        retailerstring = Retailer.lower()

        sql = "UPDATE "+retailerstring+"category2 SET item_desc = %s WHERE sku = %s"
        val = (Value, SKU)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def storecategory2Data(self, SKU, Retailer, Value):
        #print("storing sales data")
        self.insertSKU(SKU, Retailer)
        retailerstring = Retailer.lower()

        sql = "UPDATE "+retailerstring+"category2 SET drinkCat1 = %s WHERE sku = %s"
        val = (Value, SKU)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def storeBrandData(self, SKU, Retailer, Value):
        self.insertSKU(SKU, Retailer)
        retailerstring = Retailer.lower()

        sql = "UPDATE "+retailerstring+"category2 SET brand = %s WHERE sku = %s"
        val = (SKU, Value)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()
        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def storeRTDData(self, SKU, Retailer, Value):
        self.insertSKU(SKU, Retailer)
        retailerstring = Retailer.lower()

        sql = "UPDATE "+retailerstring+"category2 SET rtd = %s WHERE sku = %s"
        val = (Value, SKU)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def storeSubcategory2OneData(self, SKU, Retailer, Value):
        self.insertSKU(SKU, Retailer)
        retailerstring = Retailer.lower()

        sql = "UPDATE "+retailerstring+"category2 SET drinkCat2 = %s WHERE sku = %s"
        val = ( Value, SKU)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def storeSubcategory2TwoData(self, SKU, Retailer, Value):
        self.insertSKU(SKU, Retailer)
        retailerstring = Retailer.lower()

        sql = "UPDATE "+retailerstring+"category2 SET drinkCat3 = %s WHERE sku = %s"
        val = ( Value, SKU)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())

    def storeSubcategory2ThreeData(self, SKU, Retailer, Value):
        self.insertSKU(SKU, Retailer)
        retailerstring = Retailer.lower()

        sql = "UPDATE "+retailerstring+"category2 SET drinkCat4 = %s WHERE sku = %s"
        val = (Value, SKU)
        try:
            self.mycursor.execute(sql, val)
            self.mydb.commit()

        except Exception as e:
            print("failed to write to server with")
            print(e.__str__())



    # def storeSalesData(self, SKU, Retailer, Value, Date):
    #     #print("storing sales data")
    #     data_in = {"SKU": SKU, "Retailer" : Retailer, "Date" : Date, "Value": Value}
    #     self.sales_data = self.sales_data.append(data_in, ignore_index=True)
    #     #print( "sales data now at " + str(len(self.sales_data.index)))
    #
    # def storeUnitData(self, SKU, Retailer, Units, Date):
    #     #print("storing unit data")
    #     data_in = {"SKU": SKU, "Retailer": Retailer, "Date": Date, "Units": Units}
    #     self.unit_data = self.unit_data.append(data_in, ignore_index=True)
    #
    # def storeASPData(self, SKU, Retailer, ASP, Date):
    #     #print("storing ASP data")
    #     data_in = {"SKU": SKU, "Retailer": Retailer, "Date": Date, "ASP": ASP}
    #     self.asp_data = self.asp_data.append(data_in, ignore_index=True)