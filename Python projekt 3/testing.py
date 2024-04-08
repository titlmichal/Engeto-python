import sys
import requests
from bs4 import BeautifulSoup as bs

print(sys.argv)
try:
    uzemi = sys.argv[1]
    jmeno_souboru = sys.argv[2]
except:
    print("Nebyl zadán dostatečný počet argumentů!")
    exit()

try:
    odpoved = requests.get(uzemi)
except:
    print("Error")
    exit()
else:
    print("not error")
    if odpoved.status_code == 200:
        print(odpoved)
print("*"*30)

rozdelena_odpoved = bs(odpoved.text, features="html.parser")
tabulky = rozdelena_odpoved.find_all("table", {"class": "table"})

for tabulka in tabulky:
    for x in tabulka:
        try:
            print(x.find("td", {"class": "cislo"}).text)       #vrátí číslo obce
        except:
            continue
        try:
            print(x.find("td", headers="t1sa1 t1sb2").text)       #vrátí název obec
        except:
                try:
                    print(x.find("td", headers="t2sa1 t2sb2").text)     #vrátí název obec (když by byl 2 tabulky obcí)
                except:
                    print(x.find("td", headers="t3sa1 t3sb2").text)     #vrátí název obec (když by byl 3 tabulky obcí)
        print("https://volby.cz/pls/ps2017nss/"+x.find("a", href=True).text)       #vrátí odkaz na detailní výsledky obce
        print("*"*30)

#TADY TOHLE UŽ VYPADÁ GOOD, JEN POTŘEBA POŘEŠIT TEN ODKAZ!
