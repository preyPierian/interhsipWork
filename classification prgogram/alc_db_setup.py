from  sql_library import sql_connector 

alc_dp = sql_connector("localhost","root","root","alc_data") 
alc_dp.sql_create_table("acl_brands","(brand_name VARCHAR(255), alc_type VARCHAR(255))")
liqueurs_brands = ["bailey", "baileys", "bailey's", "Disaronno", "cointreau", "limoncello", "malibu", "Kaluha", "Drambuie", "Ouzo", "Sambuca", "Absynthe", "Sourz", "Tia Maria", "Jagermeister", "Pimms", "Pimm's", "Creme De Cassis", "Cassis", "Schnapps", "advocaat"]
wine_brands = ["RAWSONS RETREAT", "JACOB'S CREEK", "Jacobs creek", "MCGUIGAN", "yellow tail", "WOLF BLASS", "LAMBRINI", "most wanted", "barefoot", "19 crimes", "CAMPO VIEJO", "CASTIGLION", "BRUNELLO", "Tokaji", "Cellier", "MOSCATEL DE VALENCIA", "Moscatel de Chipiona", "LUSTAU", "Soleil", "Alsace", "Gewurztraminer", "TRAMBUSTI", "Chateau", "Cantin Saint Emilion", "cantine", "Marsala", "Garabaldi", "PELLEGRINO", "Barbadillo", "echo falls", "brancott", "blossom hill", "WEST COAST COOLER", "Asti Spumante", "MIONETTO", "CUVEE", "FRIZZANTE", "Beefsteak", "Bag in Box", "Puglia Rosso", "Nero d'", "Avola Sicilia", "Barton & Guestier", "Cotes de Provence", "Calvet", "Bordeaux", "Riesling"]
whiskey_brands = ["GLENFIDDICH", "chivas", "Jack Daniels", "TALISKER","Tamnavulin","Tullibardine","Tomintoul","Aberfeldy","SINGLETON OF DUFFTOWN","Penderyn Sherrywood","FAMOUS GROUSE","BOWMORE","GENTLEMAN JACK","TULLAMORE DEW","LAPHROAIG","JIM BEAM","jameson","BALVENIE","FETTERCAIRN","BRUICHLADDICH","GLENFARCLAS","LONGMORN","GLENMORANGIE","ARDBEG","HIGHLAND PARK","GLENKINCHIE","CLYNELISH","ABERLOUR","JOHNNIE","WALKER","WOODFORD","wreserve","JACK DANIEL","Southern Comfort","haig","glenlivet","redbreast","ballentines","MONKEY SHOULDER","jura"]

for x in liqueurs_brands :
    alc_dp.cursor.execute(("INSERT INTO acl_brands (brand_name,alc_type) VALUES (%s,%s) "),(x.lower(),"liqueur"))
alc_dp.db.commit()
for x in wine_brands :
    alc_dp.cursor.execute(("INSERT INTO acl_brands (brand_name,alc_type) VALUES (%s,%s) "),(x.lower(),"wine"))
alc_dp.db.commit()
for x in whiskey_brands :
    alc_dp.cursor.execute(("INSERT INTO acl_brands (brand_name,alc_type) VALUES (%s,%s) "),(x.lower(),"whiskey"))
alc_dp.db.commit()