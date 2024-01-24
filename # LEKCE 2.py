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


print("="*15, "Věci z hodiny", "="*15)
print(bool(True - True)) #False
print(bool(True - False)) #True
print(bool("")) #False
print(bool(" ")) #True
print(bool("0")) #True
print(bool(False,)) #False --> je to False a nic víc
print(bool((False,))) #True --> je tam nenulový tuple
print(bool(None)) #False --> None = absence hodnoty
print(id(1))
print(id("1"))

#CVIČENÍ V HODINĚ - počítadlo unikátních samohlásek
samohlaskove_slovo = input("Zadej slovo, kde chceš znát počet unikátních samohlásek:")
print(int("a" in samohlaskove_slovo) 
      + int("e" in samohlaskove_slovo) 
      + int("i" in samohlaskove_slovo) 
      + int("u" in samohlaskove_slovo) 
      + int("o" in samohlaskove_slovo))

#CVIČENÍ 1
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
elif moje_jmeno == "Tom":
    print("Ahoj, Tome")
elif moje_jmeno == "David":
    print("Ahoj, Davide")
elif moje_jmeno == "Jony":
    print("Ahoj, Jony")
else:
    print("Ahoj,", moje_jmeno, "e.")
print(bool(moje_jmeno == "Michal"))

tvoje_jmeno = input("Jak se jmenuješ? ")
tvuj_vek = float(input("Kolik ti je? "))
if tvuj_vek >= 18 and tvoje_jmeno == "Michal":
    print("Toooop, Michale, dám pivko")
elif tvuj_vek >= 18:
    print("Top, dáme pivko", tvoje_jmeno, "e")
elif tvoje_jmeno == "Michal" and tvuj_vek <18:
    print("Nene, Michale, ty ještě nemůžeš")
else:
    print("nedáme pivko :(((")

#CVIČENÍ V HODINĚ - průměr tříd
#Ve třídě je X studentů. Každů z nich dostal vyhodnocení testu a tvým úkolem je zjistit jaký je průměr třídy. 
#Pokud je průmer mezi 1 až 2 tak třídu pochválit, pokud mezi 2 až 4 tak konstatovat, že je to normělní protože Gauss. 
#A pokud horší než 4 tak je poslat všechny na doučování.
#Známky třídy 9A: 3,4,1,2,3,4,1,2,3,1,1,2,4
#Známky třídy 9B: 1,1,2,1,5,5,4,1,5,1,2,4,2,1,3,4
trida_a = (3,4,1,2,3,4,1,2,3,1,1,2,4)
trida_b = (1,1,2,1,5,5,4,1,5,1,2,4,2,1,3,4)
prumer_a = sum(trida_a)/len(trida_a)
prumer_b = sum(trida_b)/len(trida_b)
if prumer_a <= 2:
    print("Chválím třídu A")
elif prumer_a <= 4:
    print("To je normální, třído A, to je Gauss")
else:
    print("Třída A na doučování!")

if prumer_b <= 2:
    print("Chválím třídu B")
elif prumer_b <= 4:
    print("To je normální, třído B, to je Gauss")
else:
    print("Třída B na doučování!")



#ternární operátor: alternativní způsob
print("Ahoj, Michale") if tvoje_jmeno == "Michal" else print("Ahoj, ostatni")

#CVIČENÍ 2
print("="*15, "Cvičení 2 - Palindrom", "="*15)
zadana_slova = ["jaro", "jej", "kolo", "aha"]
slovo = zadana_slova[1]
if slovo[::-1] == slovo:
    print("Slovo", slovo, "je palindrom!")
else:
    print("Slovo", slovo, "není palindrom!")

#CVIČENÍ 3
print("="*15, "Cvičení 3 - BMI kalkulačka", "="*15)
#DOKONČIT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#METODY

#pro stringy
print("michal".upper()) #vše velké
print("michal".title()) #první velké
print("Michal".index("a")) #najde index pro a
print("Michal".replace("a", "@")) #nahradí @ za a
print("MICHAL".isupper()) #boolean zda je vše velké?
print("Ahoj, jak se máš?".split()) #rozseká string na dílky

#pro listy
seznam1 = ["a", "b", "c"]
seznam1.append("X") #přidá do listu X
print(seznam1)

print(seznam1.count("a")) #kolik "a" obsahuje list
print([1, 1, 1].count(1))

seznam2 = ["b", "d", "c", "a"]
seznam2.sort() #seřadí objekty v listu
print(seznam2)

#pro tuply
print((1, 2, 2, 2, 5).count(2)) #kolik je 2 v tuplu

print(("a", "b", "b", "c").index("c")) #na jakém indexu je "c"

#UDĚLAT CVIČENÍ PRO METODY!!!!