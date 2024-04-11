"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie (Bulls & Cows)
author: Michal Titl
email: titlmichal@gmail.com
discord: Michal_T
"""
import sys
import requests
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd


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
#tady chci vytáhnout z argumentů z konzole (index 0 je .py soubor) vyžadované argumenty - odkaz na oblast a jméno cílového filu)
#když se to nepodaří, aka třeba user to nezadá --> ende
try:
    uzemi = sys.argv[1]
    jmeno_souboru = sys.argv[2]
except:
    print("Nebyl zadán dostatečný počet argumentů!")
    exit()


#tady stahuju základní data ze zadanéhé odkazu, resp. posílám get dotaz na server a ověřuju, zda je odpověď ok
try:
    odpoved = requests.get(uzemi)
except:
    print("Error")
    exit()

#tady používám beautifulsoup knihovnu na rozparcelování získaného HTML kódu
rozdelena_odpoved = bs(odpoved.text, features="html.parser")

#úvodní stránky všech oblastí se zdají stejné, co se týče struktury, takže hledám všechny tabulky, které spadají do třídy tabulek
tabulky = rozdelena_odpoved.find_all("table", {"class": "table"})

#každá obec bude mít v tomto 1. velkém (ze 2, co se týče scrapování) slovník, kde bude mít svůj kód, název a odkaz na detailní výsledky
#proto tento seznam, kam budu každý dict nakonec sypat
dicty_obci = list()
for tabulka in tabulky:       #tabulky jsou vlastně všechny tables, tj. 1-3 tabulky (dle oblasti), každýá z nich má v sobě řádky (tr)
    for radek in tabulka:     #každá tabulka ma řádky, kde 1 řádek (který chci) má 3 td - kod, název, X (odkaz)
        dict_obce = {}
        try:
            kod_obce = radek.find("td", {"class": "cislo"}).text  #zdá se, že každý kód má tuhle třídu, která je jedinečná pro kódy
            dict_obce.update({ "kod" : kod_obce})
        except:
            continue        #tady ten try/except přístup je proto, že jsou tam i řádky tabulky, kde jsou nadpisy a jejich td nemají vlastnosti jak výše
        try:
            nazev_obce = radek.find("td", headers="t1sa1 t1sb2").text   #u názvu je to horší, protože třeba Brno nemá assignutou třídu --> dle headerů
            dict_obce.update({ "nazev" : nazev_obce})                   #každá tabulka obcí v rámci jedné oblasti má ale jiný header --> try/except níže
        except:
                try:
                    nazev_obce = radek.find("td", headers="t2sa1 t2sb2").text #když už jde o řádky druhé tabulky --> jiný druh headerů
                    dict_obce.update({ "nazev" : nazev_obce})
                except:
                    nazev_obce = radek.find("td", headers="t3sa1 t3sb2").text #když už jde o řádky třetí tabulky --> zase jiný druh headerů
                    dict_obce.update({ "nazev" : nazev_obce})
        index1 = str(radek.find("td").contents[0]).index('="')  #vytáhnout odkaz je trochu pain, protože třeba ze Brno nemá pod Xkem list, jak ostatní
        index2 = str(radek.find("td").contents[0]).index('">')  #ale seznam okresků --> univerzálnější je ten odkaz pod názvem
        odkaz_obce = "https://volby.cz/pls/ps2017nss/" + str(radek.find("td").contents[0])[index1:index2].replace("amp;", "").strip('="')
            #proto používám ty indexexy, abych to vytáhl ze stringu tagu kódu obce a očistil
        dict_obce.update({ "odkaz" : odkaz_obce})
        dicty_obci.append(dict_obce)

# for x, y in enumerate(dicty_obci):
#     print(f"Slovník číslo {x+1} je: {y}")
# print("*"*30)
#TOHLE SI TU NA TESTOVÁNÍ JEŠTĚ NECHÁM


print("ZPRACOVÁVÁM DATA ... VYČKEJTE CHVÍLI")
#ten loop dole trvá dlouho, takže proto tahle zpráva
#každopádně tohle je ten 2. velký krok (ve scrapování), kde připojím zbytek dat, resp. nakopíruju původní, který rozšířím --> proto ten list níže
rozsirene_dicty_obci = list()
for obec in dicty_obci:                                            #jeden dict = jedna obec --> každé i = jedna obec
    odkaz_obec = dicty_obci[dicty_obci.index(obec)].get("odkaz")   #vyšlu get request na odkaz v daném dictu obec z listu dictů obcí
    try:
        odpoved_obec = requests.get(odkaz_obec)
    except:
        print("Error")
        exit()
    
    rozdelena_odpoved_obec = bs(odpoved_obec.text, features="html.parser")  #pomocí BS rozparceluju odpověď
    vsechny_tables_obec = rozdelena_odpoved_obec.find_all("table")          #zajímají mě jen tabulky, takže stáhnu je
    volici_obec = vsechny_tables_obec[0]                                    #první tabulka jsou vždy obecné výsledky (voliči, obálky atd.)
    vysledky1_obec = vsechny_tables_obec[1]                                 #druhá a třetí jsou pak výsledky samotných stran
    vysledky2_obec = vsechny_tables_obec[2]                                 #naštěstí jsou v seznamu, i když dostanou 0, a seznam má vždy 2 tabulky
    
    rozsireny_dict_obce = dicty_obci[dicty_obci.index(obec)].copy()                             #zde vyrobím kopii dictu dané obce
    rozsireny_dict_obce.update({ "volici" : volici_obec.find("td", headers="sa2").text})        #a tadyy do něj dosypu voliče
    rozsireny_dict_obce.update({ "obalky" : volici_obec.find("td", headers="sa3").text})        #...obálky
    rozsireny_dict_obce.update({ "hlasy" : volici_obec.find("td", headers="sa6").text})         #... a hlasy

    vytridena_tabulka1_obec = list()                #protože mám 2 tabulky výsledků stran, tak to dělám dvakrát všechno
    vytridena_tabulka2_obec = list()                #možná by to šlo udělat hezčím způsobem, ale tohle mi nepřijde až tak hrozný ... idk
    for radek in vysledky1_obec:
        if "overflow_name" in str(radek):               #každopádně tady se koukám, jestli ve stringu řádku je overflow_name (název třídy pro název strany)
            vytridena_tabulka1_obec.append(radek)       #pokud je, tak přidám řádek do vytříděného listu řádků s výsledky
    for radek in vysledky2_obec:
        if "overflow_name" in str(radek):
            vytridena_tabulka2_obec.append(radek)
    
    rozsirenejsi_dict_obce = rozsireny_dict_obce.copy() #v rozšířeném dictu obce už jsem ty hlasy, obálky a tak --> teď kopie pro výsledky stran
    for radek in vytridena_tabulka1_obec:               #a opět nadvakrát, protože v druhé tabulce jsou jiné headers
        rozsirenejsi_dict_obce.update({radek.find("td", {"class": "overflow_name"}).text : radek.find("td", headers="t1sa2 t1sb3").text})
    for radek in vytridena_tabulka2_obec:
        rozsirenejsi_dict_obce.update({radek.find("td", {"class": "overflow_name"}).text : radek.find("td", headers="t2sa2 t2sb3").text})
                                                        #for loop vždy bere název strany jako klíč a počet hlasů jako hodnotu --> pak appendne
    
    rozsirene_dicty_obci.append(rozsirenejsi_dict_obce) #tady už pak kompletní dict obce hodím do listu kompletních dictů obcí

for slovnik in rozsirene_dicty_obci:
    for par_hodnot in slovnik:
        print(par_hodnot, slovnik[par_hodnot])
    print("*"*20)
# TOHLE SI TU NA TESTOVÁNÍ JEŠTĚ NECHÁM

#předpokládám, že v jedné oblasti budou mít ve všech obcí stejné strany - náhodný manuální check potvrzuje teorii
#tady si udělám hlavičku pomocí prvního dictu v rozšířeném listu dictů
klice_dictu = list(rozsirene_dicty_obci[0].keys())  #tady z toho dělám líst, protože keys() nevrací indexovatelný objekt
klice = klice_dictu[0:len(klice_dictu)]  #délka začína sice od 1 (indexy od 0), ale slicing nebere tu druhou krajní hodnotu (proto tam není -1)

with open(f"{jmeno_souboru}", newline="", mode="w") as file:
    zapisovac = csv.DictWriter(file, fieldnames=klice, delimiter=";")
    zapisovac.writeheader()
    for obec in rozsirene_dicty_obci:
        zapisovac.writerow(obec)
print("*" * 30)
print("OBCE ZAPSÁNY DO CSV")
