# def dataservice.storeCategoryData(SKU, Retailer, Value, category)
# brand, manufacturer, drinkCat1, drinkCat2, drinkCat3, drinkCat4, rtd
# def adjoinRules(array)
import re


#brands
liqueurs_brands = ["bailey", "baileys", "bailey's", "Disaronno", "cointreau", "limoncello", "malibu", "Kaluha", "Drambuie", "Ouzo", "Sambuca", "Absynthe", "Sourz", "Tia Maria", "Jagermeister", "Pimms", "Pimm's", "Creme De Cassis", "Cassis", "Schnapps", "advocaat"]
wine_brands = ["RAWSONS RETREAT", "JACOB'S CREEK", "Jacobs creek", "MCGUIGAN", "yellow tail", "WOLF BLASS", "LAMBRINI", "most wanted", "barefoot", "19 crimes", "CAMPO VIEJO", "CASTIGLION", "BRUNELLO", "Tokaji", "Cellier", "MOSCATEL DE VALENCIA", "Moscatel de Chipiona", "LUSTAU", "Soleil", "Alsace", "Gewurztraminer", "TRAMBUSTI", "Chateau", "Cantin Saint Emilion", "cantine", "Marsala", "Garabaldi", "PELLEGRINO", "Barbadillo", "echo falls", "brancott", "blossom hill", "WEST COAST COOLER", "Asti Spumante", "MIONETTO", "CUVEE", "FRIZZANTE", "Beefsteak", "Bag in Box", "Puglia Rosso", "Nero d'", "Avola Sicilia", "Barton & Guestier", "Cotes de Provence", "Calvet", "Bordeaux", "Riesling"]
whiskey_brands = ["GLENFIDDICH", "chivas", "Jack Daniels", "TALISKER","Tamnavulin","Tullibardine","Tomintoul","Aberfeldy","SINGLETON OF DUFFTOWN","Penderyn Sherrywood","FAMOUS GROUSE","BOWMORE","GENTLEMAN JACK","TULLAMORE DEW","LAPHROAIG","JIM BEAM","jameson","BALVENIE","FETTERCAIRN","BRUICHLADDICH","GLENFARCLAS","LONGMORN","GLENMORANGIE","ARDBEG","HIGHLAND PARK","GLENKINCHIE","CLYNELISH","ABERLOUR","JOHNNIE","WALKER","WOODFORD","wreserve","JACK DANIEL","Southern Comfort","haig","glenlivet","redbreast","ballentines","MONKEY SHOULDER","jura"]
beer_brands = ["Peroni", "Becks", "Beck's", "Budweiser", "San Miguel", "Stella Artois", "Pilsner", "Old Speckled Hen", "Leffe", "Heineken", "Hoegaarden", "Corona", "moretti", "carlsberg", "kronenbourg", "fosters", "estrella"]
beer = ["beer", "bear", "ale", "larger", "IPA", "Stout", "Shandy", ]
cider_brands = ["Thatchers", "Strongbow", "brothers"]
stout_brands = ["Guinness"]
ale_brands = ["doom bar"]
cider = ["cider", "cidre"]

beer_cider_stout_ale = ["Beer/Cider/Stout/Ale"] + beer+beer_brands+cider+cider_brands+stout_brands+ale_brands

gin_brands = ["Malfy", "GREENALLS", "bombay", "TANQUERAY", "gordon", "hendrick", "TRYYK", "CEDER", "Portobello Road", "SEEDLIP", "Sipsmith", "PLYMOUTH","beefeater"]
#TODO prioritise categories found earlier in text

wine = ["Wine","wInE","vino", "wines", "prosecco"]
sangria = ["Sangria"]

perry = ["Perry"]

cocktail = ["cocktail", "cocktails", "mojito", "pina colada", "cosmo", "cosmopolitan", "negroni", "zombie", "old fashioned", "manhattan", "margarita", "mimosa", "bellini", "paloma", "daiquiri","frappe", "bloody mary", "cuba libre", "sour mix", "gingerale", "ginger ale","soda","cola","tonic","lemonade","&lime","& lime","and lime","andlime","& diet lime","and diet lime","& spiced rum","& elderflower","gin fizz", "vodkafizz","&crmsoda","raspberry fizz"]

ginandtonic = ["Gin and tonic", "gin&tonic", "gin & tonic", "GNT", "G & T", "G&T"]
spritz = ["Spritz"]
readytodrink = ["ready to drink", "rtd", "rts", "can"]
premix = ["Premix", "pre mix", "Mixed"]
rtd_brands = ["wkd", "smirnoff ice", "schweppes", "Hooch"]
seltzer = ["Seltzer", "SLTZR", "Hard Seltzer"]

sherry = ["Sherry", "sherries"]
muscat = ["Muscat"]

vermouth = ["Vermouth"]

champagne = ["Champagne", "champange", "CHAMPAGNE"]
sparkling = ["Total Sparkling Wine", "Sparkling", "spkg", "spkl", "prosecco", "cava", "brut", "frizzante", "spumante", "spkling", "fizz"]
still = ["Still Wine", "Still"]
port = ["Port", "PORT"]

fortified = ["Fortified"]

whiskey = ["Whiskey/Bourbon", "Whiskey", "Whiskie", "Whishey", "Whisky", "Whsky", "Whiksy"]
malt = ["Malt", "mlt"]
grain = ["Grain", "rye", "corn", "wheat"]
single_malt = ["Single Malt", "sngle malt", "single mlt", "sngle mlt", "Sngl malt"]
blended = ["Blended", "blnded"]
bourbon = ["Bourbon", "borbon", "burbon"]

vodka_brands = ["Smirnoff"]

gin = ["Gin", "london dry"]

brandy = ["Brandy", "Gognac", "Armagnac", "Eau De Vie", "Pisco"]

cognac = ["Cognac"]

brandy_cognac = ["Brandy/Cognac"] + brandy + cognac

armagnac = ["Armagnac"]

vs = ["VS"]

vsop = ["VSOP", "V.S.O.P."]

xo = ["XO"]

vodka = ["Vodka"]

tequila = ["Tequila"]

mezcal = ["Mezcal"]

tequila_mezcal = ["Tequila/Mezcal"] +tequila + mezcal

liqueurs = ["Liqueurs & Speciality", "Liqueurs", "liqueur", "licor", " liqur"]

cream = ["Cream" , "creme", "crm"]
not_cream = ["Not Cream"]
red =["Red", "rouge", "noir", "tinto"]
green = ["Green", "verde"]
rose = ["Rose", "Rosé", "rosato", "rosata", "rse"]
white = ["White", "whiet", "blanc", "blanco", "bl", "Bianco"]

gold = ["Gold"]
silver = ["Silver"]
dark = ["Dark"]
pale = ["Pale"]
aged = ["Aged"]
black = ["Black"]
navy = ["Navy"]
overproof = ["Overproof"]

bitters = ["Bitters", "ANGOSTURA"]
martini = ["Martini"]

rum = ["Rum", "Rhum"]
spiced = ["Spiced", "spice", "spcd"]

rum_types = white+dark+gold+pale+spiced+aged+black+navy+overproof

spirits = [ "Spirits", "spirit"] + whiskey + gin + brandy + vodka + rum + tequila + mezcal
spirits_brands = ["bacardi", "pernod"] + vodka_brands

mulled = ["Mulled", "Mulld"]

wineTypes = still + sparkling
Pinot_Bianco = ["Pinot Bianco"]
Albarino = ["Albarino"]
Brachetto = ["Brachetto"]
Cabernet = ["Cabernet", "Carbernet", "cab"]
Cabernet_Franc = ["Cabernet Franc"]
Cabernet_Sauvignon = ["Cabernet Sauvignon", "cs"]
Chardonnay = ["Chardonnay", "chard"]
Chateau_Clerc_Milon = ["Chateau Clerc Milon", "Château Clerc Milon"]
Chenin_Blanc = ["Chenin Blanc"]
Cinsault = ["Cinsault"]
Cococciola = ["Cococciola"]
Colombard = ["Colombard", "col"]
Corvina = ["Corvina"]
Corvinone = ["Corvinone"]
Dolcetto = ["Dolcetto"]
Fiano = ["Fiano"]
Gamay = ["Gamay"]
Grenache = ["Grenache", "Garnacha"]
Gruner_Veltliner = ["Gruner Veltliner"]
Inzolia = ["Inzolia", "Ansonica"]
Lambrusco = ["Lambrusco"]
Loureiro = ["Loureiro"]
Malbec = ["Malbec"]
Merlot = ["Merlot"]
Negroamaro = ["Negroamaro"]
Orange_Muscat = ["Orange Muscat"]
Petite_Sirah = ["Petite Sirah"]
Petit_Verdot = ["Petit Verdot"]
Pinot_Blanc = ["Pinot Blanc"]
Pinot_Grigio = ["Pinot Grigio", "Pinot Gris", "PG", "Pinotgrigio", "Pinot Gri"]
Pinot_Meunier = ["Pinot Meunier"]
Pinot_Noir = ["Pinot Noir", "Pinot Nero", "Piniot Noir", "PN", "Pinotnoir"]
Pinotage = ["Pinotage"]
Riesling = ["Riesling"]
Rondinella = ["Rondinella"]
Sangiovese = ["Sangiovese"]
Sauvignon_Blanc = ["Sauvignon Blanc", "Sauv", "Sauvingnon Blanc", "sauvingon", "sav blanc"]
Semillon = ["Sémillon", "Semillon", "Sem", "Semilln"]
Shiraz = ["Shiraz", "Syrah", "Shir"]
Trebbiano = ["Trebbiano"]
Uva_di_Troia = ["Uva di Troia", "Nero di Troia"]
Vermentino = ["Vermentino"]
Viognier = ["Viognier"]
Zinfandel = ["Zinfandel", "Zinfdel"]
varietals = [Albarino, Brachetto, Cabernet, Cabernet_Franc, Cabernet_Sauvignon, Chardonnay, Chateau_Clerc_Milon, Chenin_Blanc, Cinsault, Cococciola, Colombard, Corvina, Corvinone, Dolcetto, Fiano, Gamay, Grenache, Gruner_Veltliner, Inzolia, Lambrusco, Loureiro, Malbec, Merlot, Negroamaro, Orange_Muscat, Petite_Sirah, Petit_Verdot, Pinot_Blanc, Pinot_Grigio, Pinot_Meunier, Pinot_Noir, Pinot_Bianco, Pinotage, Riesling, Rondinella, Sangiovese,  Sauvignon_Blanc, Semillon, Shiraz, Trebbiano, Uva_di_Troia, Vermentino, Viognier, Zinfandel]
white_varietals = Sauvignon_Blanc + Pinot_Blanc + Albarino + Chardonnay + Chenin_Blanc + Cococciola + Colombard + Fiano + Gruner_Veltliner + Inzolia + Loureiro + Orange_Muscat + Pinot_Blanc + Pinot_Grigio + Pinot_Meunier + Riesling + Semillon + Trebbiano + Vermentino + Viognier
red_varietals = Merlot + Malbec + Brachetto + Cabernet + Cabernet_Franc + Cabernet_Sauvignon + Chateau_Clerc_Milon + Cinsault + Corvina + Corvinone + Dolcetto + Gamay + Grenache + Lambrusco + Negroamaro + Petite_Sirah + Petit_Verdot + Pinot_Noir + Pinotage + Rondinella + Sangiovese + Shiraz + Uva_di_Troia + Zinfandel

wine_house = ["CHATEAUNEUF"]

orange = ["Orange", "org"]
pink = ["Pink", "Fruity"]
sloe = ["Sloe", "slo"]
coffee = ["coffee"]
flavours = orange + pink + sloe + coffee


def joinkeywords(arr):
    full_pattern = ""
    for word_index in range(len(arr)):
        if word_index > 0:
            full_pattern = full_pattern + "|"
        full_pattern = full_pattern + " " + arr[word_index] + " "#|"+arr[word_index]+" "

    return full_pattern

def joinkeywordslean(arr):
    full_pattern = ""
    for word_index in range(len(arr)):
        if word_index > 0:
            full_pattern = full_pattern + "|"
        full_pattern = full_pattern + " " + arr[word_index] + "|"+arr[word_index]+" "

    return full_pattern

def joinkeywordsfulllean(arr):
    full_pattern = ""
    for word_index in range(len(arr)):
        if word_index > 0:
            full_pattern = full_pattern + "|"
        full_pattern = full_pattern + arr[word_index]

    return full_pattern

def checkTextForCategory(description, retailer_text, scrape, Retailer, SKU, dataservice):

    str = description + " " + retailer_text + " " + scrape

    drinkCat1 = ""
    cat_1_pos = 9999
    drinkCat2 = ""
    cat_2_pos = 9999
    drinkCat3 = ""
    cat_3_pos = 9999
    drinkCat4 = ""
    cat_4_pos = 9999
    flavoured =  0
    rtd =  0
    str = " "+str+" "


    if len(re.findall(joinkeywordsfulllean(wine + wine_brands), str, re.IGNORECASE)) > 0:
        #dataservice.storeCategoryData(SKU, Retailer, "Wine", "drinkCat1")
        if re.search(joinkeywordsfulllean(wine + wine_brands), str, re.IGNORECASE).start() < cat_1_pos:
            drinkCat1 = wine[0]
            cat_1_pos = re.search(joinkeywordsfulllean(wine + wine_brands), str, re.IGNORECASE).start()

    for one_varietal in varietals:
        if len(re.findall(joinkeywords(one_varietal), str, re.IGNORECASE)) > 0:
            #dataservice.storeCategoryData(SKU, Retailer, "Wine", "drinkCat1")
            if re.search(joinkeywords(one_varietal), str, re.IGNORECASE).start() < cat_1_pos:
                drinkCat1 = wine[0]
                cat_1_pos = re.search(joinkeywords(one_varietal), str, re.IGNORECASE).start()

    if len(re.findall(joinkeywordsfulllean(sangria), str, re.IGNORECASE)) > 0:
        #dataservice.storeCategoryData(SKU, Retailer, "Wine", "drinkCat1")
        if re.search(joinkeywordsfulllean(sangria), str, re.IGNORECASE).start() < cat_1_pos:
            drinkCat1 = wine[0]
            drinkCat4 = sangria[0]
            cat_1_pos = re.search(joinkeywordsfulllean(sangria), str, re.IGNORECASE).start()

    if len(re.findall(joinkeywordsfulllean(vodka), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywordsfulllean(vodka), str, re.IGNORECASE).start() < cat_1_pos:
            drinkCat1 = spirits[0]
            cat_1_pos = re.search(joinkeywordsfulllean(vodka), str, re.IGNORECASE).start()
        if re.search(joinkeywordsfulllean(vodka), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat2 = vodka[0]
            cat_2_pos = re.search(joinkeywordsfulllean(vodka), str, re.IGNORECASE).start()
            ##vodka above


    #wine varietals

    if drinkCat1 == "Wine":
        #COLOURS

        if len(re.findall(joinkeywords(white), str, re.IGNORECASE)) > 0:
            drinkCat3 = white[0]
            cat_3_pos = re.search(joinkeywords(white), str, re.IGNORECASE).start()

        if len(re.findall(joinkeywords(red), str, re.IGNORECASE)) > 0:
            if re.search(joinkeywords(red), str, re.IGNORECASE).start() < cat_3_pos:
                drinkCat3 = red[0]
                cat_3_pos = re.search(joinkeywords(red), str, re.IGNORECASE).start()

        if len(re.findall(joinkeywords(rose), str, re.IGNORECASE)) > 0:
            if re.search(joinkeywords(rose), str, re.IGNORECASE).start() < cat_3_pos:
                drinkCat3 = rose[0]
                cat_3_pos = re.search(joinkeywords(rose), str, re.IGNORECASE).start()

        #IF IT HAS NOT FOUND A COLOUR ALREADY THEN LOOK FOR COLOURS BY VARIETAL
        if drinkCat3 == "":
            if len(re.findall(joinkeywords(red_varietals), str, re.IGNORECASE)) > 0:
                if re.search(joinkeywords(red_varietals), str, re.IGNORECASE).start() < cat_3_pos:
                    drinkCat3 = red[0]
                    cat_3_pos = re.search(joinkeywords(red_varietals), str, re.IGNORECASE).start()

            if len(re.findall(joinkeywords(white_varietals), str, re.IGNORECASE)) > 0:
                if re.search(joinkeywords(white_varietals), str, re.IGNORECASE).start() < cat_3_pos:
                    drinkCat3 = white[0]
                    cat_3_pos = re.search(joinkeywords(white_varietals), str, re.IGNORECASE).start()

        #TYPES
        if len(re.findall(joinkeywords(sparkling), str, re.IGNORECASE)) > 0:
            #dataservice.storeCategoryData(SKU, Retailer, sparkling[0], "drinkCat2")
            drinkCat2 = sparkling[0]
            cat_2_pos = re.search(joinkeywords(sparkling), str, re.IGNORECASE).start()

        else:
            #dataservice.storeCategoryData(SKU, Retailer, still[0], "drinkCat2")
            drinkCat2 = still[0]


        if len(re.findall(joinkeywords(mulled), str, re.IGNORECASE)) > 0:
            #dataservice.storeCategoryData(SKU, Retailer, mulled[0], "drinkCat3")
            drinkCat3 = mulled[0]
            cat_3_pos = re.search(joinkeywords(mulled), str, re.IGNORECASE).start()

        #varietals
        for one_varietal in varietals:
            if len(re.findall(joinkeywords(one_varietal), str, re.IGNORECASE)) > 0:
                if re.search(joinkeywords(one_varietal), str, re.IGNORECASE).start() < cat_4_pos:
                    drinkCat4 = one_varietal[0]
                    cat_4_pos = re.search(joinkeywords(one_varietal), str, re.IGNORECASE).start()





    if len(re.findall(joinkeywordsfulllean(fortified), str, re.IGNORECASE)) > 0:
        drinkCat1 = fortified[0]
        cat_1_pos = re.search(joinkeywordsfulllean(fortified), str, re.IGNORECASE).start()

        if len(re.findall(joinkeywords(sherry), str, re.IGNORECASE)) > 0:
            drinkCat2 = sherry[0]
            cat_2_pos = re.search(joinkeywords(sherry), str, re.IGNORECASE).start()
        elif len(re.findall(joinkeywords(port), str, re.IGNORECASE)) > 0:
            drinkCat2 = port[0]
            cat_2_pos = re.search(joinkeywords(port), str, re.IGNORECASE).start()
        elif len(re.findall(joinkeywords(muscat), str, re.IGNORECASE)) > 0:
            drinkCat2 = muscat[0]
            cat_2_pos = re.search(joinkeywords(muscat), str, re.IGNORECASE).start()

    if len(re.findall(joinkeywords(sherry), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywords(sherry), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywords(sherry), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = fortified[0]
            drinkCat2 = sherry[0]
            cat_2_pos = re.search(joinkeywords(sherry), str, re.IGNORECASE).start()
            cat_1_pos = re.search(joinkeywords(sherry), str, re.IGNORECASE).start()

    if len(re.findall(joinkeywords(port), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywords(port), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywords(port), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = fortified[0]
            drinkCat2 = port[0]
            cat_2_pos = re.search(joinkeywords(port), str, re.IGNORECASE).start()
            cat_1_pos = re.search(joinkeywords(port), str, re.IGNORECASE).start()

    if len(re.findall(joinkeywords(muscat), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywords(muscat), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywords(muscat), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = fortified[0]
            drinkCat2 = muscat[0]
            cat_2_pos = re.search(joinkeywords(muscat), str, re.IGNORECASE).start()
            cat_1_pos = re.search(joinkeywords(muscat), str, re.IGNORECASE).start()

    #wines above


    if len(re.findall(joinkeywords(gin + gin_brands + ginandtonic), str, re.IGNORECASE)) > 0 :
        if re.search(joinkeywords(gin + gin_brands + ginandtonic), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywords(gin + gin_brands + ginandtonic), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = spirits[0]
            drinkCat2 = gin[0]
            cat_1_pos = re.search(joinkeywords(gin + gin_brands + ginandtonic), str, re.IGNORECASE).start()
            cat_2_pos = re.search(joinkeywords(gin + gin_brands + ginandtonic), str, re.IGNORECASE).start()

            if len(re.findall(joinkeywords(flavours), str, re.IGNORECASE)) > 0 :
                flavoured =  1

        # for flavour in flavours:
        #     if len(re.findall(joinkeywords(flavour)) > 0:
        #         #dataservice.storeCategoryData(SKU, Retailer, flavour, "drinkCat4")

    #gins above


    if len(re.findall(joinkeywordsfulllean(whiskey + whiskey_brands) , str, re.IGNORECASE)) > 0 :
        if re.search(joinkeywordsfulllean(whiskey + whiskey_brands), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywordsfulllean(whiskey + whiskey_brands), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = spirits[0]
            drinkCat2 = whiskey[0]
            cat_1_pos = re.search(joinkeywordsfulllean(whiskey + whiskey_brands), str, re.IGNORECASE).start()
            cat_2_pos = re.search(joinkeywordsfulllean(whiskey + whiskey_brands), str, re.IGNORECASE).start()

            if len(re.findall(joinkeywordslean(malt), str, re.IGNORECASE)) > 0:
                drinkCat3 = malt[0]
                cat_3_pos = re.search(joinkeywordslean(malt), str, re.IGNORECASE).start()
                if cat_3_pos < cat_1_pos:
                    cat_1_pos = cat_3_pos
                if cat_3_pos < cat_2_pos:
                    cat_2_pos = cat_3_pos

            if len(re.findall(joinkeywordslean(grain), str, re.IGNORECASE)) > 0:
                if re.search(joinkeywordslean(grain), str, re.IGNORECASE).start() < cat_3_pos:
                    drinkCat3 = grain[0]
                    cat_3_pos = re.search(joinkeywordslean(grain), str, re.IGNORECASE).start()
                    if cat_3_pos < cat_1_pos:
                        cat_1_pos = cat_3_pos
                    if cat_3_pos < cat_2_pos:
                        cat_2_pos = cat_3_pos

            if len(re.findall(joinkeywordslean(blended), str, re.IGNORECASE)) > 0:
                cat_3_pos = re.search(joinkeywordslean(blended), str, re.IGNORECASE).start()
                drinkCat3 = blended[0]
            if len(re.findall(joinkeywordslean(bourbon), str, re.IGNORECASE)) > 0:
                cat_3_pos = re.search(joinkeywordslean(bourbon), str, re.IGNORECASE).start()
                drinkCat3 = blended[0]
                cat_4_pos = re.search(joinkeywordslean(bourbon), str, re.IGNORECASE).start()
                drinkCat4 = bourbon[0]
                # whiskeys above

    if len(re.findall(joinkeywordsfulllean(single_malt), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywordsfulllean(single_malt), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywordsfulllean(single_malt), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = spirits[0]
            cat_1_pos = re.search(joinkeywordsfulllean(single_malt), str, re.IGNORECASE).start()
            drinkCat2 = whiskey[0]
            cat_2_pos = re.search(joinkeywordsfulllean(single_malt), str, re.IGNORECASE).start()
            drinkCat3 = single_malt[0]
            cat_3_pos = re.search(joinkeywordsfulllean(single_malt), str, re.IGNORECASE).start()

    if len(re.findall(joinkeywordsfulllean(bourbon), str, re.IGNORECASE)) > 0 :
        if re.search(joinkeywordsfulllean(bourbon), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywordsfulllean(bourbon), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = spirits[0]
            cat_1_pos = re.search(joinkeywordsfulllean(bourbon), str, re.IGNORECASE).start()
            drinkCat2 = whiskey[0]
            cat_2_pos = re.search(joinkeywordsfulllean(bourbon), str, re.IGNORECASE).start()
            drinkCat3 = blended[0]
            cat_3_pos = re.search(joinkeywordsfulllean(bourbon), str, re.IGNORECASE).start()
            drinkCat4 = bourbon[0]
            cat_4_pos = re.search(joinkeywordsfulllean(bourbon), str, re.IGNORECASE).start()



    if len(re.findall(joinkeywords(brandy_cognac), str, re.IGNORECASE)) > 0 :
        if re.search(joinkeywords(brandy_cognac), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywords(brandy_cognac), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = spirits[0]
            cat_1_pos = re.search(joinkeywords(brandy_cognac), str, re.IGNORECASE).start()
            drinkCat2 = brandy_cognac[0]
            cat_2_pos = re.search(joinkeywords(brandy_cognac), str, re.IGNORECASE).start()


            if len(re.findall(joinkeywords(cognac), str, re.IGNORECASE)) > 0:
                drinkCat3 = cognac[0]

            if len(re.findall(joinkeywords(armagnac), str, re.IGNORECASE)) > 0:
                drinkCat3 = armagnac[0]

            if len(re.findall(joinkeywords(vs), str, re.IGNORECASE)) > 0:
                drinkCat4 = vs[0]

            elif len(re.findall(joinkeywords(vsop), str, re.IGNORECASE)) > 0:
                drinkCat4 = vsop[0]

            elif len(re.findall(joinkeywords(xo), str, re.IGNORECASE)) > 0:
                drinkCat4 = xo[0]


    if len(re.findall(joinkeywordsfulllean(tequila_mezcal), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywordsfulllean(tequila_mezcal), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywordsfulllean(tequila_mezcal), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = spirits[0]
            cat_1_pos = re.search(joinkeywordsfulllean(tequila_mezcal), str, re.IGNORECASE).start()
            drinkCat2 = tequila_mezcal[0]
            cat_2_pos = re.search(joinkeywordsfulllean(tequila_mezcal), str, re.IGNORECASE).start()
            if len(re.findall(joinkeywords(gold), str, re.IGNORECASE)) > 0 :
                drinkCat3 = gold[0]
                cat_3_pos = re.search(joinkeywords(gold), str, re.IGNORECASE).start()

            elif len(re.findall(joinkeywords(silver), str, re.IGNORECASE)) > 0 :
                drinkCat3 = silver[0]
                cat_3_pos = re.search(joinkeywords(silver), str, re.IGNORECASE).start()

            elif len(re.findall(joinkeywords(white), str, re.IGNORECASE)) > 0 :
                drinkCat3 = white[0]
                cat_3_pos = re.search(joinkeywords(white), str, re.IGNORECASE).start()

        #tequila above, not all defined
        ##mezcal above

    if len(re.findall(joinkeywords(rum), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywords(rum), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywords(rum), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = spirits[0]
            cat_1_pos = re.search(joinkeywords(rum), str, re.IGNORECASE).start()
            drinkCat2 = rum[0]
            cat_2_pos = re.search(joinkeywords(rum), str, re.IGNORECASE).start()

            if len(re.findall(joinkeywords(spiced), str, re.IGNORECASE)) > 0:
                drinkCat3 = spiced[0]
                cat_3_pos = re.search(joinkeywords(spiced), str, re.IGNORECASE).start()
                #rums above

            # if len(re.findall(joinkeywords(rum_types), str, re.IGNORECASE)) > 0: this neeeds fixing
            #     drinkCat3 = rum_types[0]
            #     #rums above

    if len(re.findall(joinkeywordsfulllean(liqueurs + liqueurs_brands), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywordsfulllean(liqueurs + liqueurs_brands), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywordsfulllean(liqueurs + liqueurs_brands), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = spirits[0]
            cat_1_pos = re.search(joinkeywordsfulllean(liqueurs + liqueurs_brands), str, re.IGNORECASE).start()
            drinkCat2 = liqueurs[0]
            cat_2_pos = re.search(joinkeywordsfulllean(liqueurs + liqueurs_brands), str, re.IGNORECASE).start()

            if len(re.findall(joinkeywords(cream), str, re.IGNORECASE)) > 0:
                drinkCat3 = cream[0]
                cat_3_pos = re.search(joinkeywords(cream), str, re.IGNORECASE).start()
            else:
                drinkCat3 = not_cream[0]

                #Liqueurs above

    if len(re.findall(joinkeywords(perry), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywords(perry), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywords(perry), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = perry[0]
            cat_1_pos = re.search(joinkeywords(perry), str, re.IGNORECASE).start()

    if len(re.findall(joinkeywords(bitters), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywords(bitters), str, re.IGNORECASE).start() < cat_1_pos:# and re.search(joinkeywords(bitters), str, re.IGNORECASE).start() < cat_2_pos:
            drinkCat1 = bitters[0]
            cat_1_pos = re.search(joinkeywords(bitters), str, re.IGNORECASE).start()


    if len(re.findall(joinkeywordsfulllean(martini), str, re.IGNORECASE)) > 0:

        if len(re.findall(joinkeywords(cocktail), str, re.IGNORECASE)) < 1:
            if re.search(joinkeywordsfulllean(martini), str, re.IGNORECASE).start() < cat_1_pos and re.search(joinkeywordsfulllean(martini), str, re.IGNORECASE).start() < cat_2_pos:
                drinkCat1 = fortified[0]
                cat_1_pos = re.search(joinkeywordsfulllean(martini), str, re.IGNORECASE).start()
                drinkCat2 = vermouth[0]
                cat_2_pos = re.search(joinkeywordsfulllean(martini), str, re.IGNORECASE).start()


    if len(re.findall(joinkeywordsfulllean(vermouth), str, re.IGNORECASE)) > 0 :
            if re.search(joinkeywordsfulllean(vermouth), str, re.IGNORECASE).start() < cat_2_pos:
                drinkCat1 = fortified[0]
                cat_1_pos = re.search(joinkeywordsfulllean(vermouth), str, re.IGNORECASE).start()
                drinkCat2 = vermouth[0]
                cat_2_pos = re.search(joinkeywordsfulllean(vermouth), str, re.IGNORECASE).start()

    if len(re.findall(joinkeywords(beer_cider_stout_ale), str, re.IGNORECASE)) > 0:
        if re.search(joinkeywords(beer_cider_stout_ale), str, re.IGNORECASE).start() < cat_1_pos:
            drinkCat1 = beer_cider_stout_ale[0]
            cat_1_pos = re.search(joinkeywords(beer_cider_stout_ale), str, re.IGNORECASE).start()


    if len(re.findall(joinkeywords(cocktail + ginandtonic + spritz + readytodrink + premix + rtd_brands + seltzer), description, re.IGNORECASE)) > 0:
        rtd = 1

    if len(re.findall(joinkeywordsfulllean(champagne), str, re.IGNORECASE)) > 0:
        if len(re.findall(joinkeywordsfulllean(champagne), str, re.IGNORECASE)) > 1 or len(re.findall(joinkeywordsfulllean(["Wine & Champagne"]), str, re.IGNORECASE)) < 1:
            #not an amazon mistake
            if re.search(joinkeywordsfulllean(champagne), str, re.IGNORECASE).start() < cat_1_pos:
                drinkCat1 = champagne[0]
                drinkCat2 = champagne[0]
                cat_1_pos = re.search(joinkeywordsfulllean(champagne), str, re.IGNORECASE).start()
                cat_2_pos = re.search(joinkeywordsfulllean(champagne), str, re.IGNORECASE).start()

    if len(re.findall(joinkeywords(spirits + spirits_brands), str, re.IGNORECASE)) > 0:
        #dataservice.storeCategoryData(SKU, Retailer, "Wine", "drinkCat1")
        if re.search(joinkeywords(spirits + spirits_brands), str, re.IGNORECASE).start() < cat_1_pos:
            drinkCat1 = spirits[0]
            cat_1_pos = re.search(joinkeywords(spirits + spirits_brands), str, re.IGNORECASE).start()

    if dataservice == "test":
        return {
            "drinkcat1":drinkCat1,
            "drinkcat2":drinkCat2,
            "drinkcat3":drinkCat3,
            "drinkcat4":drinkCat4,
            "flavoured":flavoured,
            "rtd":rtd
        }
    else:

        dataservice.storeCategoryData(SKU, Retailer, drinkCat1, "drinkCat1")
        dataservice.storeCategoryData(SKU, Retailer, drinkCat2, "drinkCat2")
        dataservice.storeCategoryData(SKU, Retailer, drinkCat3, "drinkCat3")
        dataservice.storeCategoryData(SKU, Retailer, drinkCat4, "drinkCat4")
        dataservice.storeCategoryData(SKU, Retailer, flavoured, "flavoured")
        dataservice.storeCategoryData(SKU, Retailer, rtd, "rtd")
