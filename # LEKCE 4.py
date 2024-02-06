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

print("="*15, "Ohlášení ve smyčkách", "="*15)
#Ohlášení ve smyčkách

#break - přeskočí zbytek smyčky
for pismeno in ["a", "b", "c", "d"]:
    if pismeno == "c":
        print("Konec smyčky, nalezno písmeno c")
        break
    print(pismeno)


#continue - přeskočí zadané
for pismeno in ["a", "b", "c", "d"]:
    if pismeno in ("a", "b"):
        continue
    print("Hodnota", pismeno, "je důležitá.")


print("="*15, "For & else", "="*15)
for pismeno in ["a", "b", "c", "d"]:
    print(pismeno.upper())
else:
    print("vše vypsáno")

for pismeno in ["a", "b", "c", "d"]:
    if pismeno == "c":
        print("našel jsem c!")
        break
else:
    print("vše jsem přošel, c tam není")        #break zruší zbytek smyčcky i else podmínku loopu for
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