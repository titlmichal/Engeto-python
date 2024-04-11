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
#   4a) podržím si číslo a název obce (pro pozdějí zápis do CSV)  - DONE
#   4b)tady bude asi nejlepší dict ve stylu kod: 123456, nazev: Adamov (--> pak budu moct zapisovat pomocí DictWriteru) - DONE
#5) sáhnu si do odkazu dané obce, kde si najdu  - DONE
#   5a) tabulku se shrnutím, kde si vezmu registrované-obálky-platné hlasy a ty uložím taky do DICTU (opět abych mohl zapisovat pomocí DictWriteru) - DONE
#   5b) tabulku se stranami, kde si vezmu název strany-počet hlasů a -----------------------------//----------------------------------------------- - DONE
#6) teď mám pro danou obec DICT se všemi klíči a hodnotami --> udělám si list, kam budu postupně sypat tyhle dicty - DONE
#7) pomocí kontextového manažera postupně zapíšu tyhle dicty do slovníku - DONE


#ZDE BUDU V KONZOLI PŘI SPOUŠTĚNÍ PROGRAMU DÁVAT 2 ARGUMENTY (link na zdroj dat scrapované oblasti a jméno výstupního souboru)
#tady chci vytáhnout z argumentů z konzole (index 0 je .py soubor) vyžadované argumenty - odkaz na oblast a jméno cílového filu)
#když se to nepodaří, aka třeba user to nezadá --> ende

def ziskej_argumenty() -> str:
    """
    Funkce ověřuje, zda uživatel zadal dostatečné množství argumentů.
    """
    try:
        uzemi = sys.argv[1]
        jmeno_souboru = sys.argv[2]
    except IndexError:
        print("Nebyl zadán dostatečný počet argumentů!")
        exit()
    return uzemi, jmeno_souboru

def zkontroluj_format(jmeno_souboru: str) -> None:
    """ 
    Funkce vyžaduje jméno souboru, kam chce uživatel zapisovat výsledky,
    a ověřuje, zda má správnou koncovku.
    """
    if jmeno_souboru[-4::] != ".csv":
        print("Nesprávný formát souboru!")
        exit()
    return None

def zkontroluj_uzemi(uzemi: str) -> requests.models.Response:
    """
    Funkce se pokouší získat odpověď serveru pomocí requestu get a skrze zadaný odkaz.
    Pokud je neúspěšná, ukončí program.
    """
    try:
        odpoved = requests.get(uzemi)
    except:
        print("Error")
        exit()
    return odpoved


def ziskej_tabulku(odpoved: requests.models.Response):
    """
    Funkce vyextrahuje ze získané odpovědi její 'textovou' formu
    a vrátí všechny tabulky s tagem tabulky a třídou tabulky, co v ní tajde.
    """
    rozdelena_odpoved = bs(odpoved.text, features="html.parser")
    tabulky = rozdelena_odpoved.find_all("table", {"class": "table"})
    return tabulky

uzemi, jmeno_souboru = ziskej_argumenty()
zkontroluj_format(jmeno_souboru)
odpoved = zkontroluj_uzemi(uzemi)
tabulky = ziskej_tabulku(odpoved)

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