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
def zkontroluj_odkaz(odkaz: str) -> requests.models.Response:
    """
    Funkce se pokouší získat odpověď serveru pomocí requestu get a skrze zadaný odkaz.
    Pokud je neúspěšná, vypíše chybu a ukončí program.
    """
    try:
        odpoved = requests.get(odkaz)
    except:
        print("Error")
        exit()
    return odpoved
def ziskej_tabulky(odpoved: requests.models.Response):
    """
    Funkce vyextrahuje ze získané odpovědi její rozpacelovanou formu dle HTML specifikace
    a vrátí všechny tabulky s tagem tabulky a třídou tabulky, co v ní tajde.
    """
    rozdelena_odpoved = bs(odpoved.text, features="html.parser")
    tabulky = rozdelena_odpoved.find_all("table", {"class": "table"})
    return tabulky
def ziskej_kod_obce(radek) -> str:
    """
    Funkce v tagu řádku tabulky hledá tag td se třídou číslo a vrací obsah jako text.
    Pokud není takový tag nalezen (což značí řádek nadpisu), vrací None a kód (v tomto případě) pokračuje.
    """
    try:
        kod_obce = radek.find("td", {"class": "cislo"}).text  #zdá se, že každý kód má tuhle třídu, která je jedinečná pro kódy
        return kod_obce
    except:
        return None
def ziskej_nazev_obce(radek) -> str:
    """
    Funkce v tagu řádku tabulky hledá tag td s headers 't1sa1 t1sb2' a vrací obsah jako text.
    Funkce se používá v návaznosti na fci ziskej_kod_obce() jejíž užití už implicitně filtruje nadpisové řádky tabulky.
    V případě, že takový tag nenajde, pokusí se získat tag s headers 't2sa1 t2sb2' odpovídající situaci, kdy scrapovaná oblast má
    více než jednu tabulku/sloupec obcí. Pokud ani zde nenajde, pokusí se získat tag s headers 't3sa1 t3sb2' odpovídající situaci, kdy scrapovaná 
    oblast má více než dvě tabulku/sloupec obcí. Vzhledem k logice zmíněné sesterské fce ziskej_kod_obce() není použita větev pro neúspěch 3 volání.
    """
    try:
        nazev_obce = radek.find("td", headers="t1sa1 t1sb2").text   #u názvu je to horší, protože třeba Brno nemá assignutou třídu --> dle headerů
    except:
            try:
                nazev_obce = radek.find("td", headers="t2sa1 t2sb2").text #když už jde o řádky druhé tabulky --> jiný druh headerů
            except:
                nazev_obce = radek.find("td", headers="t3sa1 t3sb2").text #když už jde o řádky třetí tabulky --> zase jiný druh headerů
            #!!!!DŮLEŽITÉ!!!
            #TADY UŽ return None NEDÁVÁM, PROTOŽE POKUD TO PROJDE PRVNÍ "FILTREM" (kod obce není None), TAK TADY TOHLE NEMŮŽE BÝT None
    return nazev_obce
def ziskej_odkaz_obce(radek) -> str:
    """
    Funkce vrací z prvního td tagu (tj. obsahující kód obce) odkaz na výsledky stran v dané obci řádku. Používá k tomu indexy krajních hodnot
    okolo odkazu, připojení společného začátku https adresy a formátovacích úprav.
    """
    index1 = str(radek.find("td").contents[0]).index('="')  #vytáhnout odkaz je trochu pain, protože třeba ze Brno nemá pod Xkem list, jak ostatní
    index2 = str(radek.find("td").contents[0]).index('">')  #ale seznam okresků --> univerzálnější je ten odkaz pod názvem
    odkaz_obce = "https://volby.cz/pls/ps2017nss/" + str(radek.find("td").contents[0])[index1:index2].replace("amp;", "").strip('="')
    return odkaz_obce
def aktualizuj_tabulkou_volici(tabulky, dict_obce: dict):
    """
    Funkce pomocí získaných tabulek použije tabulku, která obsahuje informace o voličích/lístcích/..., a dle vlastnotí tagů pro
    jednotlivé hledané hodnoty aktualizuje slovník obce o tyto údaje. Fce nic nevrací, jen aktualizuje.
    """
    volici_obec = tabulky[0]
    dict_obce.update({ "volici" : volici_obec.find("td", headers="sa2").text})        #a tadyy do něj dosypu voliče
    dict_obce.update({ "obalky" : volici_obec.find("td", headers="sa3").text})        #...obálky
    dict_obce.update({ "hlasy" : volici_obec.find("td", headers="sa6").text})         #... a hlasy
    return None
def ziskej_vysledky_stran(tabulky):
    """
    Cílem funkce je získat řádky obsahující výsledky jednotlivých stran. Jelikož v následném zpracování se pro namapování hledaných hodnot
    používají vlastnosti tagů, které tabulky nesdílejí, je proces zdvojen a proveden zároveň. Ze získaných tabulek jsou vybrány ty obsahující výsledky
    a do vzniknuvších listů přidávány takové řádky těchto tabulek, které obsahují sdílenou vlastnost řádků s výsledky (nikoliv nadpisy). Fce vrací
    2 listy řádků s výsledky.
    """
    vysledky1_obec = tabulky[1]                                 #druhá a třetí jsou pak výsledky samotných stran
    vysledky2_obec = tabulky[2]                                 #naštěstí jsou v seznamu, i když dostanou 0, a seznam má vždy 2 tabulky
    vytridena_tabulka1_obec = list()                #protože mám 2 tabulky výsledků stran, tak to dělám dvakrát všechno
    vytridena_tabulka2_obec = list()                #možná by to šlo udělat hezčím způsobem, ale tohle mi nepřijde až tak hrozný ... idk
    for radek in vysledky1_obec:
        if "overflow_name" in str(radek):               #každopádně tady se koukám, jestli ve stringu řádku je overflow_name (název třídy pro název strany)
            vytridena_tabulka1_obec.append(radek)       #pokud je, tak přidám řádek do vytříděného listu řádků s výsledky
    for radek in vysledky2_obec:
        if "overflow_name" in str(radek):
            vytridena_tabulka2_obec.append(radek)
    return vytridena_tabulka1_obec, vytridena_tabulka2_obec
def aktualizuj_tabulkami_stran(vytridena_tabulka1_obec: list, vytridena_tabulka2_obec: list, rozsirenejsi_dict_obce: dict) -> None:
    """
    Funkce na navazuje na fci ziskej_vysledky_stran() a pomocí z ní získaných řádků, přidávám do slovníků jednotlivých obcí informace
    o výsledcích jednotlivých stran. Fce nic nevrací.
    """
    for radek in vytridena_tabulka1_obec:               #a opět nadvakrát, protože v druhé tabulce jsou jiné headers
        rozsirenejsi_dict_obce.update({radek.find("td", {"class": "overflow_name"}).text : radek.find("td", headers="t1sa2 t1sb3").text})
    for radek in vytridena_tabulka2_obec:
        rozsirenejsi_dict_obce.update({radek.find("td", {"class": "overflow_name"}).text : radek.find("td", headers="t2sa2 t2sb3").text})
    return None
def zapis_data_do_csv(jmeno_souboru: str, rozsirene_dicty_obci: list) -> None:
    """
    Funkce zapisuje do nového souboru všechny informace o výsledcích v jednotlivých obcích. Klíče slovníků jsou použity jako hlavičky (od kódu
    obce až po poslední kandidující stranu). Fce nic nevrací.
    """
    klice_dictu = list(rozsirene_dicty_obci[0].keys())  #tady z toho dělám líst, protože keys() nevrací indexovatelný objekt
    klice = klice_dictu[0:len(klice_dictu)]  #délka začína sice od 1 (indexy od 0), ale slicing nebere tu druhou krajní hodnotu (proto tam není -1)
    with open(f"{jmeno_souboru}", newline="", mode="w") as file:
        zapisovac = csv.DictWriter(file, fieldnames=klice, delimiter=";")
        zapisovac.writeheader()
        for obec in rozsirene_dicty_obci:
            zapisovac.writerow(obec)
    return None


######################## FUNKCE VÝŠE ########################

uzemi, jmeno_souboru = ziskej_argumenty()
zkontroluj_format(jmeno_souboru)
odpoved = zkontroluj_odkaz(uzemi)
tabulky = ziskej_tabulky(odpoved)
#každá obec bude mít v tomto 1. velkém (ze 2, co se týče scrapování) slovník, kde bude mít svůj kód, název a odkaz na detailní výsledky
#proto tento seznam, kam budu každý dict nakonec sypat
dicty_obci = list()
for tabulka in tabulky:
    for radek in tabulka:
        dict_obce = {}
        if ziskej_kod_obce(radek) == None:
            continue
        kod_obce = ziskej_kod_obce(radek)
        nazev_obce = ziskej_nazev_obce(radek)
        odkaz_obce = ziskej_odkaz_obce(radek)
        dict_obce.update({ "kod" : kod_obce})
        dict_obce.update({ "nazev" : nazev_obce})
        dict_obce.update({ "odkaz" : odkaz_obce})
        dicty_obci.append(dict_obce)
print("*" * 30, "ZPRACOVÁVÁM DATA ... VYČKEJTE CHVÍLI", sep="\n")     #ten loop dole trvá dlouho, takže proto tahle zpráva - zde připojuju zbytek dat
rozsirene_dicty_obci = list()
for obec in dicty_obci:                                             #jeden dict = jedna obec --> každé i = jedna obec
    odkaz_obec = dicty_obci[dicty_obci.index(obec)].get("odkaz")
    odpoved_obec = zkontroluj_odkaz(odkaz_obec)                      #vyšlu get request na odkaz v daném dictu obec z listu dictů obcí
    vsechny_tables_obce = ziskej_tabulky(odpoved_obec)
    rozsireny_dict_obce = dicty_obci[dicty_obci.index(obec)].copy()
    aktualizuj_tabulkou_volici(vsechny_tables_obce, rozsireny_dict_obce)
    vytridena_tabulka1_obec, vytridena_tabulka2_obec = ziskej_vysledky_stran(vsechny_tables_obce)
    rozsirenejsi_dict_obce = rozsireny_dict_obce.copy() #v rozšířeném dictu obce už jsem ty hlasy, obálky a tak --> teď kopie pro výsledky stran
    aktualizuj_tabulkami_stran(vytridena_tabulka1_obec, vytridena_tabulka2_obec, rozsirenejsi_dict_obce)
    rozsirene_dicty_obci.append(rozsirenejsi_dict_obce)
zapis_data_do_csv(jmeno_souboru, rozsirene_dicty_obci)
print("*" * 30, "OBCE ZAPSÁNY DO CSV", "*" * 30, sep="\n")

############## KÓD PŘEVEDENÝ DO FCÍ VÝŠE ##############

#CO NYNÍ ZBÝVÁ:
#   dopsat rozumné komentáře do kódu, případně trošku učesat
#   vytvořit virtuální prostředí
#   vygenerovat requirements.txt soubor
#   vytvořit README.md (jak nainstalovat knihovny, jak spouštět soubor, jak funguje, případně včetně ukázky)