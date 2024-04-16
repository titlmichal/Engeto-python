"""
projekt_3.py: druhý projekt do Engeto Online Python Akademie (Bulls & Cows)
author: Michal Titl
email: titlmichal@gmail.com
discord: Michal_T
"""
import sys
import requests
from bs4 import BeautifulSoup as bs
import csv

#tady k tomu asi není moc dodat - chci po uživately argumenty, aby program věděl, odkud kam tahat
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
#tady si jen checkuju, jestli uživatel zvolil správný formát pro daný typ dat (csv)
def zkontroluj_format(jmeno_souboru: str) -> None:
    """ 
    Funkce vyžaduje jméno souboru, kam chce uživatel zapisovat výsledky,
    a ověřuje, zda má správnou koncovku.
    """
    if jmeno_souboru[-4::] != ".csv":
        print("Nesprávný formát souboru!")
        exit()
    return None
#tady naopak ověřuji, jestli je odkaz v pořádku
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
#tady už je to imo zajímavější: ze získané odpovědi serveru "vyextrahuji" základní tabulky, se kterými budu dál pracovat
#takže použiju beautifulsoup na textovanou odpověď a najdu si všechny objekty s tagem tabulky a třídou tabulka
def ziskej_tabulky(odpoved: requests.models.Response):
    """
    Funkce vyextrahuje ze získané odpovědi její rozpacelovanou formu dle HTML specifikace
    a vrátí všechny tabulky s tagem tabulky a třídou tabulky, co v ní tajde.
    """
    rozdelena_odpoved = bs(odpoved.text, features="html.parser")
    tabulky = rozdelena_odpoved.find_all("table", {"class": "table"})
    return tabulky
#pro splnění zadání i další kroky programu potřebuju kód obce, naštěstí to vypadá, že všechny kódy  mají pro svou skupinu unikátní vlastnosti
#funkci používám při procházení každé tabulky řádek po řádku a zároveň částečně filtruji ty řádky, které se netýkají hard dat (skryté řádky, nadpisy, ...)
#princip je, že v daném řádků hledám tag s danou třídou ... protože je tam jeden takový, tak stačí jednoduché find
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
#s názvy je to trochu komplikovanější, takže i funkce je (o něco) komplexnější
#každá scrapovaná oblast může mít 1-3 tabulky obcí, přičemž první tabulka používá jiné headers (nebo nějaký jiný unikátní identifikátor) než ty ostatní 2
#a protože procházení řádků nechci komplikovat (cíl byl, ať je prochází jen jednou), tak používám try/except ve stylu if/elif/else
#ve výsledku pak sice může 2./3. tabulka být náročnější, na druhou stranu, pokud nenastane nějaké moje "osobní" černá labuť, tak by tu neměl nastat problém
#jinak princip je obdobný jak u kódu obce (vlastně téměř stejný)
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
#s odkazem jsem trochu bojoval, protože mi přišlo lepší si sáhnout na odkaz výsledků celé obce, než ještě procházet případně okresky a lepit je dohromady
#ten "dobrý odkaz" se nachází jako hyperlink právě v kódu obce, takže si pro něj sahám do stringu daného td tagu
#respektive si tam pomáhám metodou contents a hledám index, kde (+-) začíná, a index, kde +- končí onen odkaz
#z toho stejného stringu si ho pak vyparsuju, přilepím k němu začátek a zbavím vzniklého šumu
def ziskej_odkaz_obce(radek) -> str:
    """
    Funkce vrací z prvního td tagu (tj. obsahující kód obce) odkaz na výsledky stran v dané obci řádku. Používá k tomu indexy krajních hodnot
    okolo odkazu, připojení společného začátku https adresy a formátovacích úprav.
    """
    index1 = str(radek.find("td").contents[0]).index('="')  #vytáhnout odkaz je trochu pain, protože třeba ze Brno nemá pod Xkem list, jak ostatní
    index2 = str(radek.find("td").contents[0]).index('">')  #ale seznam okresků --> univerzálnější je ten odkaz pod názvem
    odkaz_obce = "https://volby.cz/pls/ps2017nss/" + str(radek.find("td").contents[0])[index1:index2].replace("amp;", "").strip('="')
    return odkaz_obce
#tady použím vyextrahované tabulky v 2. hlavní scrapovací částí (tj. data o samotných obcích) a vzniklé dicty obci, kde každá obec má svůj dict
#kde má kód, název a odkaz
#první vyextrahovaná tabulka jsou vždy obecné informace o voličích, takže stačí index
#a pak už jen updatuju daný slovník o nové páry klíč/hodnoty, přičemž hodnoty hledám podobně jako předchozí data (daný tag a unikátní vlastnost)
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
#tady ze získaných tabulek pro danou obci používám ty zbývající 2, které se týkají výsledků kandidujících stran
#jak vysvětluju v docstringu, tabulky používají jiné headers, skrze které pak v nich hledám hodnoty, tak je proces zdvojen, tedy:
#uložím tabulku, nachystám list na výsledky, pro každý řádek v tabulce se podívám, zda v jeho string formě není daný text (to je název třídy obsahující
# hard dat, ne headers apod.), pokud ano, hodím ho do listu (v původním formátu)...to stejné pro druhou tabulku
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
#tady je vidět to, co jsem popisoval v komentáři výše - v každém řádku hledám název strany a počet hlasů
#název stran je v tagu, který by se hledal dobře v obou zároveň, to ale není pravda o počtu hlasů
#každopádně podobně jako u rozšiřování slovníku obce o voliče, tak podobně aktualizuji slovník o výsledky voleb, jen hledám i klíč
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
#tady si už jen vezmu název souboru, jak zadal uživatel, a list dictů obcí s hledanými hodnotami, který mezitím program vytvořil, a nasypu jej do csv
#předpokládám stejnou kandidátků v celé oblasti, takže používám jako headers klíče z prvního slovníku
#pro samotný zápis pak použiju DictWriter metodu, kvůli které jsem asi celou dobu směřoval ke slovníkům nebo prostě to tak hezky vyšlo, idk
#a pak už jen sypu obec po obci :)
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



if __name__ == "__main__":
    uzemi, jmeno_souboru = ziskej_argumenty()           #ziskám základní argumenty z inputu v konzoli
    zkontroluj_format(jmeno_souboru)                    #ověřím formát zadaného názvu souboru
    odpoved = zkontroluj_odkaz(uzemi)                   #ověřím a uložím odpověď serveru na zadaný odkaz
    tabulky = ziskej_tabulky(odpoved)                   #získám tabulky s obcemi v dané oblasti
    #každá obec bude mít v tomto 1. velkém (ze 2, co se týče scrapování) slovník, kde bude mít svůj kód, název a odkaz na detailní výsledky
    #proto tento seznam, kam budu každý dict nakonec sypat
    dicty_obci = list()                                 #viz předchozí komentář
    for tabulka in tabulky:                             #tabulek je/může být více, takže chci projít vždy jednu po druhé
        for radek in tabulka:                           #funkce mi stojí hlavně na řádcích, takže projdu vždy tabulku řádek po řádku
            dict_obce = {}                              #nachystám si první dict pro danou obec
            if ziskej_kod_obce(radek) == None:          #pokud daný řádek neobsahuje data o obci (je to hlavička, skrytý řádek ...) --> přeskočím
                continue
            kod_obce = ziskej_kod_obce(radek)           #vezmu si kód obce
            nazev_obce = ziskej_nazev_obce(radek)       #........její název
            odkaz_obce = ziskej_odkaz_obce(radek)       #........a odkaz na detalní výsledky
            dict_obce.update({ "kod" : kod_obce})       #a o tyhle informace obohatím daný slovník obce
            dict_obce.update({ "nazev" : nazev_obce})   #-----------------//---------------------------
            dict_obce.update({ "odkaz" : odkaz_obce})   #-----------------//---------------------------
            dicty_obci.append(dict_obce)                #pak jen dict přihodím do listu dictů
    print("*" * 30, "ZPRACOVÁVÁM DATA ... VYČKEJTE CHVÍLI", sep="\n")     #ten loop dole trvá dlouho, takže proto tahle zpráva - zde připojuju zbytek dat
    rozsirene_dicty_obci = list()                                         #nechci používat původní list, sahat tam a upravovat a zase vracet, takže nový
    for obec in dicty_obci:                                               #z uložených dat/dictů obce si už ziskám zbytek
        odkaz_obec = dicty_obci[dicty_obci.index(obec)].get("odkaz")      #vezmu odkaz na výsledky dané obce
        odpoved_obec = zkontroluj_odkaz(odkaz_obec)                       #ověřím/získám odpověď
        vsechny_tables_obce = ziskej_tabulky(odpoved_obec)                #z odpovědi vytáhnu tabulky dané obce
        rozsireny_dict_obce = dicty_obci[dicty_obci.index(obec)].copy()   #vytvořím kopiii původního slovníku, kam dosypu zbyývají data
        aktualizuj_tabulkou_volici(vsechny_tables_obce, rozsireny_dict_obce)
                                                                          #rozšiřím slovník o data ohledně voličů
        vytridena_tabulka1_obec, vytridena_tabulka2_obec = ziskej_vysledky_stran(vsechny_tables_obce)
                                                                          #vezmu si tabulky s výsledky stran kandidujících v obci
        rozsirenejsi_dict_obce = rozsireny_dict_obce.copy()               #opět si udělám kopii před další aktualizací
        aktualizuj_tabulkami_stran(vytridena_tabulka1_obec, vytridena_tabulka2_obec, rozsirenejsi_dict_obce)
                                                                          #a tady udělám tu finální aktualizaci o výsledky jednotlivých stran v obci
        rozsirene_dicty_obci.append(rozsirenejsi_dict_obce)               #výsledný dict pak je hodím k ostatním, které tím nachystám k zápisu
    zapis_data_do_csv(jmeno_souboru, rozsirene_dicty_obci)                #zápišu data do tabulky
    print("*" * 30, "OBCE ZAPSÁNY DO CSV", "*" * 30, sep="\n")            #řeknu uživateli, že je hotovo


#CO NYNÍ ZBÝVÁ:
#   vytvořit README.md (jak nainstalovat knihovny, jak spouštět soubor, jak funguje, případně včetně ukázky)