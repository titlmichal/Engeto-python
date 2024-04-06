"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie (Bulls & Cows)
author: Michal Titl
email: titlmichal@gmail.com
discord: Michal_T
"""
import sys
import requests
from bs4 import BeautifulSoup as bs

print(sys.argv)
#ZDE BUDU V KONZOLI PŘI SPOUŠTĚNÍ PROGRAMU DÁVAT 2 ARGUMENTY (link na zdroj dat scrapované oblasti a jméno výstupního souboru)
uzemi = sys.argv[1]
jmeno_souboru = sys.argv[2]
print(uzemi)
print(jmeno_souboru)

#KDYŽ JE ODKAZ ŠPATNĚ, tak to hodí nesmyslně dlouhý error message, ale odpověď serveru je 200 --> ošetřuju jedno po druhém
#TAK TO O ŘÁDEK VÝŠE ASI NENÍ PRAVDA --> MUSÍM ZJISTIT A ZAKOMPONOVAT !!!
try:
    odpoved = requests.get(uzemi)
except:
    print("Error")
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