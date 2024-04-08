"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie (Bulls & Cows)
author: Michal Titl
email: titlmichal@gmail.com
discord: Michal_T
"""
import sys
import requests
from bs4 import BeautifulSoup as bs


#GAMEPLAN JAK NA TO PŮJDU
#CÍLOVÉ HEADERS CSV: kód-lokace-registrovaných-obálek-platné hlasy-KAŽDÁ kandidující STRANA 1 sloupec
#1) vezmu si od uživatele odkaz na oblast, kterou chce scrapovat, a název csv, kam to dát - DONE
#2) ověřím, že:
#   2a) odkaz je vpoho  - DONE
#   2b) název souboru je vpoho
#3) stáhnu obsah stránky z odkazu  - DONE
#4) najdu si tabulka/table rows, kde je číslo obce, název obce a odkaz na výsledky v dané obci  - DONE
#   4a) podržím si číslo a název obce (pro pozdějí zápis do CSV)
#   4b)tady bude asi nejlepší dict ve stylu kod: 123456, nazev: Adamov (--> pak budu moct zapisovat pomocí DictWriteru)
#5) sáhnu si do odkazu dané obce, kde si najdu
#   5a) tabulku se shrnutím, kde si vezmu registrované-obálky-platné hlasy a ty uložím taky do DICTU (opět abych mohl zapisovat pomocí DictWriteru)
#   5b) tabulku se stranami, kde si vezmu název strany-počet hlasů a -----------------------------//-----------------------------------------------
#6) teď mám pro danou obec DICT se všemi klíči a hodnotami --> udělám si list, kam budu postupně sypat tyhle dicty
#7) pomocí kontextového manažera postupně zapíšu tyhle dicty do slovníku


print(sys.argv)
#ZDE BUDU V KONZOLI PŘI SPOUŠTĚNÍ PROGRAMU DÁVAT 2 ARGUMENTY (link na zdroj dat scrapované oblasti a jméno výstupního souboru)
try:
    uzemi = sys.argv[1]
    jmeno_souboru = sys.argv[2]
except:
    print("Nebyl zadán dostatečný počet argumentů!")
    exit()
else:
    print(uzemi)
    print(jmeno_souboru)

#KDYŽ JE ODKAZ ŠPATNĚ, tak to hodí nesmyslně dlouhý error message, ale odpověď serveru je 200 --> ošetřuju jedno po druhém
#TAK TO O ŘÁDEK VÝŠE ASI NENÍ PRAVDA --> MUSÍM ZJISTIT A ZAKOMPONOVAT !!!
try:
    odpoved = requests.get(uzemi)
except:
    print("Error")
    exit()
else:
    print("not error")
    if odpoved.status_code == 200:
        print(odpoved)
        #print(odpoved.text)
    # elif odpoved.status_code in range(300, 400):
    #     print("Chyba přesměrování")
    # elif odpoved.status_code in range(400, 500):
    #     print("Chyba klienta")
    # elif odpoved.status_code in range(500, 600):
    #     print("Chyba serveru")
    # else:
    #     print("NEZNÁMÁ CHYBA!")
print("*"*30)

rozdelena_odpoved = bs(odpoved.text, features="html.parser")
#print(rozdelena_odpoved.prettify())

#Z ODPOVĚDI MĚ BUDE ZAJÍMAT asi nejspíš td class="cislo" (cislo obce, tam je i HYPERTEXT), td class="overfow_name" (nazev obce)
#TY JSOU ALE V TABULKÁCH, TAKŽE BYCH SI MĚL ASI ŠÁHNOUT PRVNĚ PRO NĚ... table class="table"
vhodne_tridy = ("cislo", "overflow_name", "center")
# vsechny_td = rozdelena_odpoved.find_all("td")
# for i in vsechny_td:
#     print(i)
vsechny_tr = rozdelena_odpoved.find_all("tr")
vytridene_tr = list()
for i in vsechny_tr:
    if 'class="cislo"' in str(i):
        vytridene_tr.append(i)
for i in vytridene_tr:
    print(i, "\n", ".......")
print("*"*30)

# dicty_obci = list()
# for x, y in enumerate(vsechny_td):
#     dict_obce = {
#         "kod" : 0,
#         "nazev" : 0,
#         "odkaz" : 0
#     }
#     if x in range(0, len(vsechny_td)+1, 3) and "hidden_td" not in str(y):
#         print("Tohle je kod ...", str(y)[112:118])
#     elif x in range(1, len(vsechny_td)+1, 3) and "hidden_td" not in str(y):
#         print("Tohle je nazev ...", str(y)[48:48+str(y)[48:80].index("<")])
#     elif x in range(2, len(vsechny_td)+1, 3) and "hidden_td" not in str(y):
#         print("Tohle je odkaz ...", "https://volby.cz/pls/ps2017nss/"+str(y)[44:105])
#     else:
#         continue
#     dicty_obci.append(dict_obce)
# for x, y in enumerate(dicty_obci):
#     print(f"Tohle je dict číslo {x}, obsahuje: {y}")

tabulky = rozdelena_odpoved.find_all("table", {"class": "table"})

for tabulka in tabulky:
    for x in tabulka:
        print(x.find("td", {"class": "cislo"}).text)       #vrátí číslo obce
        try:
            print(x.find("td", headers="t1sa1 t1sb2").text)       #vrátí název obec
        except:
            try:
                print(x.find("td", headers="t2sa1 t2sb2").text)
            except:
                print(x.find("td", headers="t3sa1 t3sb2").text)
        print("https://volby.cz/pls/ps2017nss/"+x.find("a", href=True).text)       #vrátí odkaz na detailní výsledky obce
        print("*"*30)
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #TADY TOHLE MUSÍM UPRAVIT, PROTOŽE TŘEBA PRO PRAHU TO NEBUDE FUNGOVAT, PROTOŽE JE TAM KRATŠÍ ODKAZ SKRZE KRATŠÍ ČÍSLO KRAJE A TAK
    #MÍSTO TOHO BYCH TO MĚL UDĚLAT, JAK DOLE PRO VÝSLEDKY - ROZDĚLIT NA TABLE DATA A POUŽÍT .text
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #UPDATE 7.4.2024 21:15: tady jsem se snažil to vyřešit s tím komplikovaným slicingem/strindigem, ale ještě to není ono
    #resp issue je ten, že 1) for loop hodí 4 Benešov (když to dám na okres Benešov žejo) a 2) mi nejde vytáhntou ten odkaz zatím
    #měl bych se imo podívat do toho, jak to scrapuju a podle toho upravit/upravit scrapování
    #nemyslím, že to je těžké, jen už mi teď hlava moc nefunguje i guess :D
    #good luck next time! <3
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#teď vím, jak si vytáhnout kód, název a odkaz jednotlivých obcí --> TEĎ BYCH Z TOHO UDĚLAL DICT PRO KAŽDOU OBEC VE STYLU "nazev" :nazev_obce, ...
#PAK JE NAHÁZÍM DO LISTU, NA KTERÝ PAK BUDU MOC APLIKOVAT FOR SMYČKU (z každého dictu vytáhnut odkaz a zpracuju data z odkazu)
#po zpracování dat z odkazu ještě musím vymyslet, jak s tím naložím (přidat nová data k původním slovníku z listu X vytvořit nový?)
#asi bych SPÍŠ VYTVOŘIL NOVÝ Z KOPIE PŮVODNÍHO --> budu mít list dictů, který "jen" dictWriterem zapíšu

dicty_obci = list()
for i in vytridene_tr:
    dict_obce = {}
    dict_obce.update({ "kod" : str(i)[117:123]})
    dict_obce.update({ "nazev" : str(i)[181:181+str(i)[181:220].index("<")]})
    dict_obce.update({ "odkaz" : "https://volby.cz/pls/ps2017nss/"+str(i)[str(i).index("<a href=")+9:115].replace("amp;", "")})
    dicty_obci.append(dict_obce)

#!!!!!!!!!!!!!!!!!!!!!!!!
#TADY KONČÍ ZÍSKÁVÁNÍ DICTŮ OBCÍ (KOD, NÁZEV, ODKAZ), NA KTERÝCH PAK STAVÍM ZBYTEK
#!!!!!!!!!!!!!!!!!!!!!!!!

for x, y in enumerate(dicty_obci):
    print(f"Slovník číslo {x+1} je: {y}")
print("*"*30)

#TAK ... teď mám list dictů, kde každý dict je jedna obce a jejíc kód, název a odkaz na detilní výsledky
#TAKŽE TEĎ JE NA ČASE VYTÁHNOUT DATA Z VÝSLEDKOVÉ STRÁNKY PRO KAŽDÝ DICT OBCE
#UDĚLÁM TO PRO JEDEN A PAK ZBYTEK BUDU ŘEŠIT LOOPEM (až to budu dávat do fce)
odkaz_obec1 = dicty_obci[0].get("odkaz")

#bude mě zajímat první tabulka (table id="ps311_t1") a druhá tabulka (tabulky v divech class="t2_470")
try:
    odpoved_obec1 = requests.get(odkaz_obec1)
except:
    print("Error")
    exit()
else:
    print("not error")
    if odpoved_obec1.status_code == 200:
        print(odpoved_obec1)
        #print(odpoved.text)
    # elif odpoved.status_code in range(300, 400):
    #     print("Chyba přesměrování")
    # elif odpoved.status_code in range(400, 500):
    #     print("Chyba klienta")
    # elif odpoved.status_code in range(500, 600):
    #     print("Chyba serveru")
    # else:
    #     print("NEZNÁMÁ CHYBA!")
print("*"*30)

rozdelena_odpoved_obec1 = bs(odpoved_obec1.text, features="html.parser")
# print(rozdelena_odpoved_obec1.prettify())
vsechny_tables_obec1 = rozdelena_odpoved_obec1.find_all("table")
volici_obec1 = vsechny_tables_obec1[0]
vysledky1_obec1 = vsechny_tables_obec1[1]
vysledky2_obec1 = vsechny_tables_obec1[2]

# list_vysledku_obec1 = list()
# list_vysledku_obec1.append(vsechny_tables_obec1[1])
# list_vysledku_obec1.append(vsechny_tables_obec1[2])
# print(list_vysledku_obec1)
    #BTW třeba Praha má 3 sloupečky obcí, tak idk, jestli mi to někde nerozbije logiku

#TADY MÁM ROZDĚLENÉ TABULKY VÝSLEDKŮ O POČTECH VOLIČŮ/HLASŮ A 2 TABULKY PRO VÝSLEDKY DLE STRAN
#TEĎ MUSÍM VYTÁHNOUT INFO O VOLIČÍCH - voliči v seznamu, vydané obálky, platné hlasy
#td voličů v seznamu má unique headers="sa2", vydané obálky headers="sa3" a platné hlasy headers="sa6"

# for x, y in enumerate(volici_obec1):
#     print(f"Tohle je tag číslo {x+1}, obsahuje: {y}")
print("*"*30)
print("Tady je počet voličů v seznamu:", volici_obec1.find("td", headers="sa2").text)       #sebevysvětlující docela ...
print("Tady je počet vydaných obálek:", volici_obec1.find("td", headers="sa3").text)         #sebevysvětlující docela ...
print("Tady je počet platných hlasů:", volici_obec1.find("td", headers="sa6").text)          #sebevysvětlující docela ...

#TEĎ MÁM DALŠÍ ČÁST TABULKY: POČTY VOLIČŮ, OBÁLEK A PLATNÝCH HLASŮ --> PŘIDAT DO DICTU
rozsireny_dict_obce1 = dicty_obci[0].copy()
rozsireny_dict_obce1.update({ "volici" : volici_obec1.find("td", headers="sa2").text})
rozsireny_dict_obce1.update({ "obalky" : volici_obec1.find("td", headers="sa3").text})
rozsireny_dict_obce1.update({ "hlasy" : volici_obec1.find("td", headers="sa6").text})
print(rozsireny_dict_obce1)
print("*"*30)

#TAK TEĎ MÁM UŽ DALŠÍ VĚCI V DICTU, SICE JEN PRO JEDNU OBEC ALE MÍSTO INDEXU 0 BYCH POUŽIL i V LOOPU A UDĚLAL TO PRO VŠE
#TEĎ JE ČAS VYTÁHNOUT VOLEBNÍ VÝSLEDKY - POZOR: TENTOKRÁT BUDOU KLÍČE STRANY A HODNOTY POČET HLASŮ, CO DOSTALY
#TADY MĚ ZAJÍMAJÍ td class="overflow_name" a td headers="t1sa2 t1sb3" (nebo "t2sa2 t2sb3" pro druhou tabulku)

for x, y in enumerate(vysledky1_obec1):
    print(f"Tohle je tag číslo {x}, obsahuje: {y}")
print("*"*30)

vytridena_tabulka1_obec1 = list()
vytridena_tabulka2_obec1 = list()
for i in vysledky1_obec1:
    if "overflow_name" in str(i):
        vytridena_tabulka1_obec1.append(i)
for i in vysledky2_obec1:
    if "overflow_name" in str(i):
        vytridena_tabulka2_obec1.append(i)

#hledám podle headerů a druhá tabulka má jiný --> používám oddělené seznamy, tj. 2 for loopy

rozsirenejsi_dict_obce1 = rozsireny_dict_obce1.copy()
print(rozsirenejsi_dict_obce1)

print(vytridena_tabulka1_obec1[0])
for i in vytridena_tabulka1_obec1:
    print(i.find("td", {"class": "overflow_name"}).text)
    print(i.find("td", headers="t1sa2 t1sb3").text)
    rozsirenejsi_dict_obce1.update({ i.find("td", {"class": "overflow_name"}).text : i.find("td", headers="t1sa2 t1sb3").text})
for i in vytridena_tabulka2_obec1:
    print(i.find("td", {"class": "overflow_name"}).text)
    print(i.find("td", headers="t2sa2 t2sb3").text)
    rozsirenejsi_dict_obce1.update({ i.find("td", {"class": "overflow_name"}).text : i.find("td", headers="t2sa2 t2sb3").text})

for i in rozsirenejsi_dict_obce1:
    print(i, rozsirenejsi_dict_obce1[i])

#TAKŽE TEĎ MÁM FINÁLNÍ SLOVNÍK PRO JEDNU OBCI ... JUCHŮŮŮŮ
#TEĎ TO MUSÍM UPRAVIT TAK, ABY TO DĚLALO PRO KAŽDOU OBCI
print("*"*30)

#!!!!!!!!!!!!!!!!!!!!!!!!
#TADY NAVAZUJI NA PŮVODNÍ ZÍSKÁVÁNÍ DICTU OBCÍ (kde je zatím jen kód, název a odkaz) a ZÍSKÁVÁM ZDE ZBYTEK DAT
#!!!!!!!!!!!!!!!!!!!!!!!!

print("ZPRACOVÁVÁM DATA ... VYČKEJTE CHVÍLI")
rozsirene_dicty_obci = list()
for i in dicty_obci:
    odkaz_obec = dicty_obci[dicty_obci.index(i)].get("odkaz")
    try:
        odpoved_obec = requests.get(odkaz_obec)
    except:
        # print("Error")
        exit()
    # else:
    #     print("not error")
    # if odpoved_obec.status_code == 200:
    #     print(odpoved_obec)
        #print(odpoved.text)
    # elif odpoved.status_code in range(300, 400):
    #     print("Chyba přesměrování")
    # elif odpoved.status_code in range(400, 500):
    #     print("Chyba klienta")
    # elif odpoved.status_code in range(500, 600):
    #     print("Chyba serveru")
    # else:
    #     print("NEZNÁMÁ CHYBA!")
    
    rozdelena_odpoved_obec = bs(odpoved_obec.text, features="html.parser")
    # print(rozdelena_odpoved_obec1.prettify())
    vsechny_tables_obec = rozdelena_odpoved_obec.find_all("table")
    volici_obec = vsechny_tables_obec[0]
    vysledky1_obec = vsechny_tables_obec[1]
    vysledky2_obec = vsechny_tables_obec[2]
    
    rozsireny_dict_obce = dicty_obci[dicty_obci.index(i)].copy()
    rozsireny_dict_obce.update({ "volici" : volici_obec.find("td", headers="sa2").text})
    rozsireny_dict_obce.update({ "obalky" : volici_obec.find("td", headers="sa3").text})
    rozsireny_dict_obce.update({ "hlasy" : volici_obec.find("td", headers="sa6").text})

    vytridena_tabulka1_obec = list()
    vytridena_tabulka2_obec = list()
    for i in vysledky1_obec:
        if "overflow_name" in str(i):
            vytridena_tabulka1_obec.append(i)
    for i in vysledky2_obec:
        if "overflow_name" in str(i):
            vytridena_tabulka2_obec.append(i)
    
    rozsirenejsi_dict_obce = rozsireny_dict_obce.copy()
    for i in vytridena_tabulka1_obec:
        # print(i.find("td", {"class": "overflow_name"}).text)
        # print(i.find("td", headers="t1sa2 t1sb3").text)
        rozsirenejsi_dict_obce.update({ i.find("td", {"class": "overflow_name"}).text : i.find("td", headers="t1sa2 t1sb3").text})
    for i in vytridena_tabulka2_obec:
        # print(i.find("td", {"class": "overflow_name"}).text)
        # print(i.find("td", headers="t2sa2 t2sb3").text)
        rozsirenejsi_dict_obce.update({ i.find("td", {"class": "overflow_name"}).text : i.find("td", headers="t2sa2 t2sb3").text})
    
    rozsirene_dicty_obci.append(rozsirenejsi_dict_obce)

for slovnik in rozsirene_dicty_obci:
    for par_hodnot in slovnik:
        print(par_hodnot, slovnik[par_hodnot])
    print("*"*20)

#!!!!!!!!!!!!!!!!!!!!!!!!
#TADY JSEM ZÍSKAL ZBYTEK. VÝSLEDEK NÁHODNÉ VALIDACE: okres Prostějov vypadá GOOOOD
#!!!!!!!!!!!!!!!!!!!!!!!!

#TEĎ JE ČAS TO HODIT DO CSVéčka!
#prnvě bych si měl najít nejdelší dict --> TEN BUDE MÍT VŠECHNY STRANY
for slovnik in rozsirene_dicty_obci:
    print(len(slovnik), "...", )