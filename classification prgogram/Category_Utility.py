# def dataservice.storeCategoryData(SKU, Retailer, Value, category)
# brand, manufacturer, drinkCat1, drinkCat2, drinkCat3, drinkCat4, rtd
# def adjoinRules(array)

# Changes by preya : 
#  - Added category object, stores category information and update methods
# need to do vlaidation 

from genericpath import exists
import re
from category_obj import category_object


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


def checkTextForCategory(description, retailer_text, scrape, Retailer, SKU, dataservice):
    str = description + " " + retailer_text + " " + scrape
    current_item = category_object(str)

    if current_item.exsits(wine + wine_brands) and current_item.first_pos(wine + wine_brands) < current_item.cat_1_pos:
        current_item.update_category(1,wine[0],wine + wine_brands)
            
    for one_varietal in varietals:
        if current_item.exsits(one_varietal) and current_item.first_pos(one_varietal) < current_item.cat_1_pos:
            current_item.update_category(1,wine[0],one_varietal)
    
    
    if current_item.exsits(sangria) and current_item.first_pos(sangria) < current_item.cat_1_pos :
        current_item.update_category(1,wine[0],sangria)
        current_item.update_category(4,sangria[0],sangria)
    
    if current_item.exsits(vodka) :
        if current_item.first_pos(vodka) < current_item.cat_1_pos:
            current_item.update_category(1,spirits[0],vodka)
        if current_item.first_pos(vodka) < current_item.cat_2_pos:
            current_item.update_category(2,vodka[0],vodka)
            ##vodka above
    
      #wine varietals

    if current_item.drinkCat1 == "Wine":
        #COLOURS

        if current_item.exsits(white):
            current_item.update_category(3,white[0],white)

        if current_item.exsits(red):
            current_item.update_category(3,red[0],red)

        if current_item.exsits(rose):
            current_item.update_category(3,rose[0],rose)

        #IF IT HAS NOT FOUND A COLOUR ALREADY THEN LOOK FOR COLOURS BY VARIETAL
        if current_item.drinkCat3 == "":
            if current_item.exsits(red_varietals):
                current_item.update_category(3,rose[0],red_varietals)

            if current_item.exsits(white_varietals):
                current_item.update_category(3,rose[0],white_varietals)
        #TYPES
        if current_item.exsits(sparkling):
            current_item.update_category(2,sparkling[0],sparkling) 
        else:
            #dataservice.storeCategoryData(SKU, Retailer, still[0], "drinkCat2")
            current_item.update_category(2,still[0],"") 

        if current_item.exsits(mulled):
            current_item.update_category(3,mulled[0],mulled) 

        #varietals
        for one_varietal in varietals:
            if current_item.exsits(one_varietal):
                if  current_item.first_pos(one_varietal) < current_item.cat_4_pos:
                    current_item.update_category(4,one_varietal[0],one_varietal)

        if current_item.exsits(fortified) :
            current_item.update_category(1,fortified[0],fortified)

            if current_item.exsits(sherry) :
                current_item.update_category(2,sherry[0],sherry)
            elif current_item.exsits(port) :
                current_item.update_category(2,port[0],port)
            elif current_item.exsits(muscat) :
                current_item.update_category(2,muscat[0],muscat)

        if current_item.exsits(sherry):
            if current_item.first_pos(sherry) < current_item.cat_1_pos and current_item.first_pos(sherry) < current_item.cat_2_pos :
                current_item.update_category(1,fortified[0],sherry)
                current_item.update_category(2,sherry[0],sherry)
                
        if current_item.exsits(port):
            if current_item.first_pos(port) < current_item.cat_1_pos and current_item.first_pos(port) < current_item.cat_2_pos :
                current_item.update_category(1,fortified[0],port)
                current_item.update_category(2,muscat[0],port)   

        if current_item.exsits(muscat):
            if current_item.first_pos(muscat) < current_item.cat_1_pos and current_item.first_pos(muscat) < current_item.cat_2_pos :
                current_item.update_category(1,fortified[0],muscat)
                current_item.update_category(2,muscat[0],muscat) 
        
        #wines above
    if current_item.exsits(whiskey + whiskey_brands):
        if current_item.first_pos(whiskey + whiskey_brands) < current_item.cat_1_pos and current_item.first_pos(whiskey + whiskey_brands) < current_item.cat_2_pos :
            current_item.update_category(1,spirits[0],whiskey + whiskey_brands)
            current_item.update_category(2,whiskey[0],whiskey + whiskey_brands)             

            if current_item.exsits(malt) :
                current_item.update_category(3,malt[0],malt)
                if current_item.cat_3_pos < current_item.cat_1_pos :
                    current_item.cat_1_pos = current_item.cat_3_pos
                if current_item.cat_3_pos < current_item.cat_2_pos:
                    current_item.cat_2_pos = current_item.cat_3_pos

            if current_item.exsits(grain) :
                current_item.update_category(3,grain[0],grain)
                if current_item.cat_3_pos < current_item.cat_1_pos :
                    current_item.cat_1_pos = current_item.cat_3_pos
                if current_item.cat_3_pos < current_item.cat_2_pos:
                    current_item.cat_2_pos = current_item.cat_3_pos

  

            if current_item.exsits(blended):
                current_item.update_category(3,blended[0],blended)

            if current_item.exsits(bourbon):
                current_item.update_category(3,blended[0],bourbon)
                current_item.update_category(4,bourbon[0],bourbon)
                # whiskeys above


    if current_item.exsits(gin + gin_brands + ginandtonic) :
        if current_item.first_pos(gin + gin_brands + ginandtonic) < current_item.cat_1_pos and current_item.first_pos(gin + gin_brands + ginandtonic) < current_item.cat_2_pos :
            current_item.update_category(1,spirits[0],gin + gin_brands + ginandtonic)
            current_item.update_category(2,gin[0],gin + gin_brands + ginandtonic) 
            if current_item.exsits(flavours) :
                current_item.update_flavour(True)
        # for flavour in flavours:
        #     if len(re.findall(joinkeywords(flavour)) > 0:
        #         #dataservice.storeCategoryData(SKU, Retailer, flavour, "drinkCat4")

    #gins above

    if current_item.exsits(single_malt):
        if current_item.first_pos(single_malt) < current_item.cat_1_pos and current_item.first_pos(single_malt) < current_item.cat_2_pos :
            current_item.update_category(1,spirits[0],single_malt)
            current_item.update_category(2,whiskey[0],single_malt)
            current_item.update_category(3,single_malt[0],single_malt)

    if current_item.exsits(bourbon):
            if current_item.first_pos(bourbon) < current_item.cat_1_pos and current_item.first_pos(bourbon) < current_item.cat_2_pos :
                current_item.update_category(1,spirits[0],bourbon)
                current_item.update_category(2,whiskey[0],bourbon)
                current_item.update_category(3,blended[0],bourbon)
                current_item.update_category(4,bourbon[0],bourbon)

    if current_item.exsits(brandy_cognac) :
           if current_item.first_pos(brandy_cognac) < current_item.cat_1_pos and current_item.first_pos(brandy_cognac) < current_item.cat_2_pos :
            current_item.update_category(1,spirits[0],brandy_cognac)
            current_item.update_category(2,brandy_cognac[0],brandy_cognac)

            if current_item.exsits(cognac):
                current_item.update_category(3,cognac[0],cognac)

            if current_item.exsits(armagnac):
                current_item.update_category(3,armagnac[0],armagnac)
        
            
            if current_item.exsits(vs):
                current_item.update_category(4,vs[0],vs)
            elif current_item.exsits(vsop):
                current_item.update_category(4,vsop[0],vsop)
            elif current_item.exsits(xo):
                current_item.update_category(4,xo[0],xo)

    if current_item.exsits(tequila_mezcal):
        if current_item.first_pos(tequila_mezcal) < current_item.cat_1_pos and current_item.first_pos(tequila_mezcal) < current_item.cat_2_pos :
            current_item.update_category(1,spirits[0],tequila_mezcal)
            current_item.update_category(2,tequila_mezcal[0],tequila_mezcal)
            

            if current_item.exsits(gold):
                current_item.update_category(3,gold[0],gold)
            elif current_item.exsits(silver):
                current_item.update_category(3,silver[0],silver)
            elif current_item.exsits(white):
                current_item.update_category(3,white[0],white)

        #tequila above, not all defined
        ##mezcal above
    if current_item.exsits(rum):
        if current_item.first_pos(rum) < current_item.cat_1_pos and current_item.first_pos(rum) < current_item.cat_2_pos :
            current_item.update_category(1,spirits[0],rum)
            current_item.update_category(2,rum[0],rum)

            if current_item.exsits(spiced):
             current_item.update_category(3,spiced[0],spiced)
                #rums above

            # if len(re.findall(joinkeywords(rum_types), str, re.IGNORECASE)) > 0: this neeeds fixing
            #     drinkCat3 = rum_types[0]
            #     #rums above

    if current_item.exsits(liqueurs + liqueurs_brands):
        if current_item.first_pos(liqueurs + liqueurs_brands) < current_item.cat_1_pos and current_item.first_pos(liqueurs + liqueurs_brands) < current_item.cat_2_pos :
            current_item.update_category(1,spirits[0],liqueurs + liqueurs_brands)
            current_item.update_category(2,liqueurs[0],liqueurs + liqueurs_brands)

            if  current_item.exsits(cream):
                current_item.update_category(3,cream[0],cream)
            else:
                current_item.drinkCat3 = not_cream[0]

                #Liqueurs above

    if  current_item.exsits(perry) :
        if current_item.first_pos(perry) < current_item.cat_1_pos and current_item.first_pos(perry) < current_item.cat_2_pos :
            current_item.update_category(1,perry[0],perry)

    if  current_item.exsits(bitters) :
        if current_item.first_pos(bitters) < current_item.cat_1_pos :
            current_item.update_category(1,bitters[0],bitters)

    if current_item.exsits(martini) :
        if current_item.exsits(cocktail):
             if current_item.first_pos(martini) < current_item.cat_1_pos and current_item.first_pos(martini) < current_item.cat_2_pos :
                current_item.update_category(1,fortified[0],martini)
                current_item.update_category(2,vermouth[0],martini)

    if current_item.exsits(vermouth) :
            if current_item.first_pos(vermouth) < current_item.cat_2_pos:
                current_item.update_category(1,fortified[0],vermouth)
                current_item.update_category(2,vermouth[0],vermouth)

    if current_item.exsits(beer_cider_stout_ale) :
            if current_item.first_pos(beer_cider_stout_ale) < current_item.cat_1_pos:
                current_item.update_category(1,beer_cider_stout_ale[0],beer_cider_stout_ale)

    

    if current_item.exsits(cocktail + ginandtonic + spritz + readytodrink + premix + rtd_brands + seltzer):
        current_item.update_rtd(True)


    if current_item.exsits(champagne):
        #if len(re.findall(joinkeywordsfulllean(champagne), str, re.IGNORECASE)) > 1 or len(re.findall(joinkeywordsfulllean(["Wine & Champagne"]), str, re.IGNORECASE)) < 1:
            #not an amazon mistake
            if current_item.first_pos(champagne) < current_item.cat_1_pos:
                current_item.update_category(1,champagne[0],champagne)
                current_item.update_category(2,champagne[0],champagne)
    
    if current_item.exsits(spirits + spirits_brands):
        #dataservice.storeCategoryData(SKU, Retailer, "Wine", "drinkCat1")
        if current_item.first_pos(spirits + spirits_brands) < current_item.cat_1_pos:
            current_item.update_category(1,spirits[0],spirits + spirits_brands)

    if dataservice == "test":
        return {
            "drinkcat1":current_item.drinkCat1,
            "drinkcat2":current_item.drinkCat2,
            "drinkcat3":current_item.drinkCat3,
            "drinkcat4":current_item.drinkCat4,
            "flavoured":current_item.flavoured,
            "rtd":current_item.rtd
        }
    else:

        dataservice.storeCategoryData(SKU, Retailer, current_item.drinkCat1, "drinkCat1")
        dataservice.storeCategoryData(SKU, Retailer, current_item.drinkCat2, "drinkCat2")
        dataservice.storeCategoryData(SKU, Retailer, current_item.drinkCat3, "drinkCat3")
        dataservice.storeCategoryData(SKU, Retailer, current_item.drinkCat4, "drinkCat4")
        dataservice.storeCategoryData(SKU, Retailer, current_item.flavoured, "flavoured")
        dataservice.storeCategoryData(SKU, Retailer, current_item.rtd, "rtd")


""" def joinkeywords(arr):
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

    return full_pattern """