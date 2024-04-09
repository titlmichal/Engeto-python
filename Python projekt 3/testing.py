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

for tabulka in tabulky:       #tabulky jsou vlastně všechny tables, tj. 1-3 tabulky (dle oblasti), každýá z nich má v sobě řádky (tr)
    for radek in tabulka:     #každá tabulka ma řádky, kde 1 řádek (který chci) má 3 td - kod, název, X (odkaz)
        try:
            print(radek.find("td", {"class": "cislo"}).text)       #vrátí číslo obce
        except:
            continue
        try:
            print(radek.find("td", headers="t1sa1 t1sb2").text)       #vrátí název obec
        except:
                try:
                    print(radek.find("td", headers="t2sa1 t2sb2").text)     #vrátí název obec (když by byl 2 tabulky obcí)
                except:
                    print(radek.find("td", headers="t3sa1 t3sb2").text)     #vrátí název obec (když by byl 3 tabulky obcí)
        index1 = str(radek.find("td").contents[0]).index('="')
        index2 = str(radek.find("td").contents[0]).index('">')
        print("https://volby.cz/pls/ps2017nss/" + str(radek.find("td").contents[0])[index1:index2].replace("amp;", "").strip('="'))
                    #vrátí odkaz na detail obce
        print("*"*30)

#TADY TOHLE UŽ VYPADÁ GOOD, dokonce jsem vytáhnl odkaz na obci!
#(btw nehledám název obce dle třídy, protože třeba Brno ji nemá!)
