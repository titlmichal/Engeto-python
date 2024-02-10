# LEKCE 5

nazev_lekce = "LEKCE 5"
delka_nazvu_lekce = len(nazev_lekce)
print("="*15, nazev_lekce, "="*15)
print("-" * (30 + delka_nazvu_lekce + 2),)

print("="*15, "WHILE LOOP", "="*15)
i = 0
while i < 5:
    print("Hodnota i je ", i)
    i = i + 1
print("i dosáhlo 5 --> konec smyčky")

#podmínka ve smyčce
i = 0
while i < 10:
    if i % 2 == 0:
        print("Index je: ", i)
    i = i + 1
print("Konec smyčky")

#ohlášení ve smyčkách
i = 0
while i < 10:
    i = i + 1
    print("i je: ", i)          #BTW ZAJÍMAVÉ: když dám tenhle print nad přičtení, 1 hodnotou i bude 0, když nechám zde, tak 1 (makes sense)
    if i == 4:
        print("Smyčka dosáhla definované hodnoty 4")
        break

i = 0
while i <= 19:
    i = i + 1                   #když by tohle tady nebylo --> NEKONEČNÁ SMYČKA
    if i % 2 == 0:
        continue                #CONTINUE slouží na pokračování na ZAČÁTEK --> zde tzn., že když je i dělitelné 2, vrátí se na začátek (nevypíše zde print)
    print("i je nyní: ", i)

i = 0
while i < 10:
    i = i + 1
    print("Index i je nyní: ", i)       #zase tady docela záleží na cíli programu --> dle toho dát i = i+1 nad/pod a jiný znamínka v podmínce apod.
else:
    print("Hodnota indexu", i, "byla dovršena s podmínkou --> konec")
    #POZOR - BREAK přeruší i to pod else(!) - viz níže

i = 0
while i < 10:
    i = i + 1
    print("Hodnota i je nyní: ", i)
    if i == 5:
        print("Dosažena hodnota ", i, "--> konec smyčky")
        break
else:
    print("Hodnota indexu", i, "byla dovršena s podmínkou --> konec")

print("="*15, "NEKONEČNÁ SMYČKA", "="*15)
#tohle je vykomentované, protože je to ta neřízené --> nekončí
i = 1
# while i > 0:
#    print(i)
#    i = i + 1

#řízená nekonečná smyčka
dotazovani = True
while dotazovani:
    odpoved = input("Zadej hodnotu mezi 1 a 5: ")
    if odpoved.isnumeric() and int(odpoved) in range(1, 6):
        print("Správně jsi zadal/a hodnotu!")
        dotazovani = False
    else:
        print("Hodnotu jsi nezadal dle pokynů!")

#řízená nekonečná smyčka bez pomocné proměnné
while True:
    odpoved = input("Zadej hodnotu mezi 1 a 5: ")
    if odpoved.isnumeric() and int(odpoved) in range(0, 6):
        print("Správně jsi zadal/a hodnotu!")
        break
    else:
        print("Hodnotu jsi nezadal dle pokynů!")

#CVIČENÍ 1
print("="*15, "Cvičení 1 - Ukládej slova", "="*15)
slova = list()
while len(slova) < 3:
    slovo = input("Zadej slovo o délce 4 znanků: ".lower())
    if slovo in slova:
        print(f"Slovo {slovo} už je uložené")
        continue
    elif len(slovo) != 4:
        print(f"Slovo není dlouhé čtyři znaky")
        continue
    else:
        slova.append(slovo)
print("Už mám uložené tři slova")

#CVIČENÍ 2
print("="*15, "Cvičení 2 - Přeruš výběr", "="*15)
ovoce = ("jablko", "banan", "citron", "pomeranc")
print("Dostupné ovoce:",  ", ".join(ovoce))
while True:
    vyber = input("VYBER Z DOSTUPNÉHO OVOCE: ")
    if vyber.lower() in ovoce:
        print("Bezva, toto ovoce je v nabídce.")
        break
    else:
        print("Ovoce není v nabídce.")

#CVIČENÍ 3
print("="*15, "Cvičení 3 - Kalkulačka", "="*15)
print("Vítej v kalkulačce. Tato kalkulačka umí jen + a -.")
while True:
    operation = input("Vyber + nebo -: ").strip()
    if operation in ("+", "-"):
        number_1 = input("Zadej první číslo: ")
        number_2 = input("Zadej druhé číslo: ")
        if operation == "+":
            print(number_1, operation, number_2, "=", int(number_1) + int(number_2))
        elif operation == "-":
            print(number_1, operation, number_2, "=", int(number_1) - int(number_2))
        dalsi_operace = input("Chcete provést další operaci?('a' pro ano, jakákoliv jiná klávesa pro ne): ")
        if dalsi_operace == "a":
            continue
        else:
            print("Nashledanou")
            break
    else:
        print("Nezadali jste platný operátor, zkuste to znovu")

print("="*15, "PŘIŘAZOVACÍ OPERÁTOR", "="*15)
print(jmeno := "Michal")
# v podmínce
cislo = 5
if (umocnene_cislo := cislo ** 2) <= 30:
    print(f"Číslo {umocnene_cislo} umocněné na druhou je menší než 30")
else:
    print("Není menší")
#ve smyčce while
while (vstup := input("--> ")) != "quit":
    print("Zadal jsi: ", vstup)
else:
    print("Konec smyčky")