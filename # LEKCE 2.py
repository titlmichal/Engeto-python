# LEKCE 2
nazev_lekce = "LEKCE 2"
delka_nazvu_lekce = len(nazev_lekce)
print("="*15, nazev_lekce, "="*15)
print("-" * (30 + delka_nazvu_lekce + 2),)

print(1 > 2) #FALSE
print(1000 > 10) #TRUE
print(True == 1) #TRUE
print(False == 0) #TRUE
print(bool(2 > 1)) #TRUE
print(bool(5 != 1)) #TRUE
print("="*15, "Srovnávání", "="*15)
print(10 >= 10)
print(10 == 10)
print(11 == 11)
print(4 != 5)
print(5 != 5)
print("="*15, "Boolean procesy", "="*15)
#porovnávání identit
print(id(1))
print(id("a"))
moje_cislo_2 = 2
print(id(moje_cislo_2))
moje_cislo_1 = 1
print(moje_cislo_1 is moje_cislo_2) #FALSE
print(moje_cislo_1 is not moje_cislo_2) #TRUE
cislo1 = 1
cislo2 = 1
print(cislo1 is cislo2) #TRUE
#operátory
print(True and True) #TRUE
print(True and False) #FALSE
print(False and False) #FALSE
print(True or False) #TRUE
print(True or True) #TRUE
print(False or False) #FALSE
print(not True) #FALSE
print(not False) #TRUE
#ověřování členství
print("M" in "Michal") #TRUE
print("#" in "Michal") #FALSE
print("x" not in "Michal") #TRUE
print("="*15, "Cvičení 1 - List, indexování", "="*15)
zamestnanci = [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]
posledni_index = len(zamestnanci) - zamestnanci[::-1].index(zamestnanci[-1]) - 1 #jako asi by to nemuselo být tak komplikované a prostě tam mít délka -1 _D
print("Na indexu 2 je:", zamestnanci[2])
print("Na", posledni_index, "indexu je:", zamestnanci[-1])
print("V intervalu od 2 do 5 je:", zamestnanci[2:6])
print("Každý třetí člen je:", zamestnanci[::3])

#PODMÍNKY
moje_jmeno = input("Zadejte jmeno ")
if moje_jmeno == "Michal":
    print("Ahoj, Michale")
else:
    print("Ahoj, ostatní, kteří se nejmenujete Michal!")
print(bool(moje_jmeno == "Michal"))