# LEKCE 4

nazev_lekce = "LEKCE 4"
delka_nazvu_lekce = len(nazev_lekce)
print("="*15, nazev_lekce, "="*15)
print("-" * (30 + delka_nazvu_lekce + 2),)

print("="*15, "FOR LOOP", "="*15)
#for loop
for cislo in [1, 2, 3, 4, 5]:           #lze iterovat list ...
    print(cislo)
for pismeno in ["a", "b", "c", "d"]:    #...list složený ze stringů
    print(pismeno)
for pismeno in "michal":                #...string
    print(pismeno)
for pismeno in ("x", "y", "z"):         #...tuple
    print(pismeno)
for klice in {"jmeno": "michal", "prijmeni": "xyz", "vek": 24}:     #...slovník
    print(klice)
for symbol in {"#", "@", "&"}:          #... i set (ale bez pořadá)
    print(symbol)

print("="*15, "For loop a slovníky", "="*15)
#skrze klíče
osoba = {
    "jmeno": "Matous",
    "prijmeni": "Holinka",
    "email": "matous@holinka.com"
}
for klic in osoba:
    print(klic, osoba[klic], sep="=") #defaultně jde skrze klíče --> prvně dá klíč --> pak chceme hodnoty, tak si o něj musím říct viz osoba[klic]

osoba = {
    "jmeno": "Matous",
    "prijmeni": "Holinka",
    "email": "matous@holinka.com"
}
for klic in osoba.keys():
    print(klic, osoba[klic], sep="=")

#skrze kombinaci
osoba = {
    "jmeno": "Matous",
    "prijmeni": "Holinka",
    "email": "matous@holinka.com"
}
for klic, hodnota in osoba.items():
    print(klic, hodnota, sep="=")

#skrze hodnoty - je to blbý, protože klíče se sice nemohou opakovat ve slovníku, ale hodnoty ano --> blbě se pak zpětně zjišťuje, která hodnota odpovídá čemu
osoba = {
    "jmeno": "Matous",
    "prijmeni": "Holinka",
    "email": "matous@holinka.com"
}
for hodnota in osoba.values():
    print(hodnota)

print("="*15, "Podmínky ve smyčce", "="*15)
#podmínky ve smyčce
suda_cisla = list()
licha_cisla = list()
for cislo in (1, 2, 3, 4, 5, 6, 7):
    if cislo % 2 == 0:        #pokud je číslo sudé (zbytek po dělení 2 je nula)
        suda_cisla.append(cislo) #přidej do seznamu suda_cisla cislo
    else:
        licha_cisla.append(cislo)
print(suda_cisla)
print(licha_cisla)

pismena = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
for pismeno in pismena:
    if pismeno == "g":
        print("*Mám hodnotu ->*", pismeno)
    else:
        print("Nemám g, ale", pismeno)

for pismeno in pismena:
    if pismeno == "g":
        print("*Mam hodnotu ->*", pismeno)      #vypíše jen u g, ale v pozadí to bude probíhat dál --> když by tam bylo další g --> vypíše další
#to se hodí třeba na testování, zda něco tam je (třeba tam dát místo print přičtení do nějaké proměnné), ale pro hledání --> ohlášení ve smyčkách

print("="*15, "Ohlášení ve smyčkách", "="*15)
#Ohlášení ve smyčkách

#break - přeskočí zbytek smyčky
for pismeno in ["a", "b", "c", "d"]:
    if pismeno == "c":
        print("Konec smyčky, nalezno písmeno c")
        break       #zde skončí celý cyklus
    print(pismeno)
list_cisel = [1,2,3,4,5]
for cislo in list_cisel:
    print(cislo, end="")    #zde se přiřadí 1ka a vypíše se
    continue                #zde je ohlášení ke přeskočení zbytku bloku
    print(cislo)            #skrze continue dojde k přeskočení této částí bloku skončí první iterace a jde se na další --> výsledek: 12345


#continue - přeskočí zadané: např. chceme vykonat kód jen pokud osoba je žena (apod.) ... lze to nahradit if else, ale continue to dělá čitelnější
for pismeno in ["a", "b", "c", "d"]:
    if pismeno in ("a", "b"):
        continue
    print("Hodnota", pismeno, "je důležitá.")

#pass - nedělej nic --> k zabránění syntax error
list_cisel = [1,2,3,4,5]
for cislo in list_cisel:
    print(cislo, end="")
    pass                    #je to "výplňové slovo --> zde vlastně nic neudělá"
    print(cislo)
#ale zde se to může hodit, abych nemusel třeba psát pod if print(), jen abych nedostal chybu
soucet = 0
for cislo in list_cisel:
    if (cislo % 2) == 0: # sude cislo
        pass # nemuzeme tento blok nechat prazdny, proto pouzijeme pass - jinak nema vyznam
    else:
        soucet += cislo
print(soucet)

print("="*15, "Cvičení na počítání písmen v hodině", "="*15)
veta = """V době hospodářského pokulhávání se Německo pouští do zajímavého experimentu. 
Několik stovek zaměstnanců po celé zemi totiž počátkem února začne pracovat jen čtyři dny v týdnu, a to při zachování původní výše mzdy. 
Cílem je zjistit, zda zaměstnanci mohou být v případě přechodu na kratší pracovní týden nejen zdravější a spokojenější, ale rovněž i produktivnější."""
vysledek = 0
for pismena in veta:
    if pismena.lower() == "o" or pismena.lower() == "a":
        vysledek = vysledek + 1
print(vysledek)
#POZOR: tohle šlo napsat skrze metodu snadněji: veta.count("o") + veta.count("a")

print("="*15, "For & else", "="*15)
for pismeno in ["a", "b", "c", "d"]:
    print(pismeno.upper())
else:
    print("vše vypsáno")            #to else má trochu jiný význam než u if, pokud je odsazené s for

for pismeno in ["a", "b", "c", "d"]:
    if pismeno == "c":
        print("našel jsem c!")
        break
else:
    print("vše jsem přošel, c tam není")        #break zruší zbytek smyčcky i else podmínku loopu for...prostě skončí celý cyklus
print("Pokračuji...")

print("="*15, "Zanořená smyčka", "="*15)
jmena = [
    ["Matous", "Marek", "Lukas", "Jan"],
    ["Lucie", "Aneta", "Eva", "Lenka"],
    ["Helmut", "Hammet", "Hetfield", "Harold"]
]
for jmeno in jmena:             #jde index po index --> vypíše [0], [1], [2], ..., ale už ne [0][0], [0][1] atd.
    print(jmeno)

#vnořené for
for seznam in jmena:            #prvně uloží do proměnné seznam obsah prvního indexu jmena (["Matous", "Marek", "Lukas", "Jan"])
    for jmeno in seznam:        #...pak z proměnné seznam (kde jsou ty jména z prvního indexu výše), uloží do proměnné jméno postupně hodnoty ze seznamu
        print(jmeno)            #...každou hodnotu jmeno vypíše a vrátí se ke vnějšímu for, kde uloží do seznamu ["Lucie", "Aneta", "Eva", "Lenka"]
                                #...a celé zopakuje


#CVIČENÍ 1
print("="*15, "Cvičení 1 - Počty čísel", "="*15)
sequence = [1, 21, 5, 3, 5, 8, 321, 1, 2, 2, 32, 6, 9, 1, 4, 6, 3, 1, 2]
counts = {}
for cislo in sequence:
    if cislo not in counts:
        counts[cislo] = 1
    else:
        counts[cislo] = counts.get(cislo) + 1
for cislo in dict(sorted(counts.items())):
    print("key:", cislo, "value:", counts[cislo])

#CVIČENÍ 2
print("="*15, "Cvičení 2 - Ze stringu seznam", "="*15)
vysledek = []
zadana_cisla = "1, 2, 3, 4, 5"
cisla = zadana_cisla.split(",")
for numbers in cisla:
    vysledek.append(int(numbers))
print("List:", vysledek)

#CVIČENÍ 3
print("="*15, "Cvičení 3 - Samohlásky a souhlásky", "="*15)
veta = "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu"
samohlasky = "aeiouy"
vysledek = {"souhlasky": 0, "samohlasky": 0}
for pismena in veta:
    if pismena.isspace():
        continue
    if pismena in samohlasky:
        vysledek["samohlasky"] = vysledek.get("samohlasky") + 1
    else:
        vysledek["souhlasky"] = vysledek.get("souhlasky") + 1
print("Počet souhlásek:", vysledek["souhlasky"], "| Počet samohlásek:", vysledek["samohlasky"])

#CVIČENÍ 4
print("="*15, "Cvičení 4 - Sudá vs. lichá", "="*15)
cisla = [1, 2, 3, 4, 5, 6, 7, 8]
suda = 0
licha = 0
for numbers in cisla:
    if numbers % 2 == 0:
        suda = suda + numbers
    elif numbers % 2 != 0:
        licha = licha + numbers
vysledek = abs(suda - licha)
print("Rozdíl je:", vysledek)


print("="*15, "RANGE, ENUMERATE", "="*15)
rozsah = range(12)
print(rozsah)               #je to specifické v tom, že printne doslova range(0, 12) ...
print(type(rozsah))
#1 argument                 #neobsahuje poslední prvek, aby se to dalo používat na indexování (dám limit délku něčeho --> poslední index by byl přes limit)
print(tuple(range(11)))     #...proto tam dáváme ten tuple/list apod.
#2 argumenty
print(tuple(range(2, 11)))  #číslo OD BUDE součástí výstupu, číslo DO součástí NEBUDE
#3 argumenty
print(tuple(range(2, 11, 3)))

print(tuple(range(0, 10, -1)))      #vrátí (), protože jdeme od nuly do mínusu --> mezi 0 a 10 není nic v mínusu
print(tuple(range(10, 0, -1)))      #vrátí tuple od 10 do 1, protože jde po mínus jedničce od 10 do 0 --> 10 -1 = 9; 9 -1 = 8; ...

print("="*15, "Smyčka a range", "="*15)
for cislo in range(7):
    print(cislo)

for vypis in range(5):
    print("Vypíše 5krát toto:", vypis)

print("="*15, "Funkce ENUMERATE", "="*15)
jmena = ("C", "Rust", "Java", "Python")
print(list(enumerate(jmena)))

#smyčka a enumerate
for pismeno in enumerate("Ahoj, světe"):
    print(pismeno)

for index, symbol in enumerate("Ahoj, světe"):
    print(f"Index: {index}, symbol: {symbol}")

print("="*15, "Funkce ZIP", "="*15)
#spojí dva 2 sekvenční prvky dohromady
jmena = ("Petr", "Marek", "David")
prijmeni = ("Svetr", "Pavel", "Dvořák")
print(list(zip(jmena, prijmeni)))

print("X"*25, "DODĚLAT CVIČENÍ", "X"*25)

print("#"*25, "UDĚLAT DOMÁCÍ ÚKOL", "#"*25) #cílem je zjistit 3 nejčastější slova

print("&"*25, "UDĚLAT PRVNÍ PROJEKT V PYTHONU", "&"*25)