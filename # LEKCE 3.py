# LEKCE 3
nazev_lekce = "LEKCE 3"
delka_nazvu_lekce = len(nazev_lekce)
print("="*15, nazev_lekce, "="*15)
print("-" * (30 + delka_nazvu_lekce + 2),)

print("="*15, "Slovníky", "="*15)
#slovníky
muj_slovnik = {"jmeno": "Michal", "registrovany": True, "vek": 24}
print(muj_slovnik)
print(type(muj_slovnik))
prazdny_slovnik = {}
print(type(prazdny_slovnik))
slovnik_skrze_fci = dict(jmeno = "Michal", vek = 25) #zde KLASICKÉ ZÁVORKY! když je to skrz fci
print(slovnik_skrze_fci)

#hledání hodnot ve slovníku = mapování
print(slovnik_skrze_fci["jmeno"], slovnik_skrze_fci["vek"])

#ukládání klíčů
slovnik1 = {}
slovnik1["jmeno"] = "michal"
print(slovnik1)
slovnik1["jmeno"] = "titl"
print(slovnik1) # --> přepíše na titl

#zapisování a vkládání hodnot
slovnik2 = {}
slovnik2["jmeno"] = "Michal"
slovnik2["vek"] = 23
slovnik2["ridicak"] = True
slovnik2["kontakt"] = "Brno, 625 00"
print(slovnik2)
print(slovnik2["ridicak"])
print(slovnik2["jmeno"])

#vnořená datová struktura
info = {}
kontakty = {"telefon" : "+420 739 123 456", "email" : "michal@gmail.com"}
info["kontakty"] = kontakty
print(info["kontakty"])
print(info["kontakty"]["telefon"])

print("="*15, "Metody slovníků", "="*15)
#metody slovníků
print(muj_slovnik.items())                            #vrátí klíče i hodnoty jako tuple
print(muj_slovnik.get("jmeno"))                       #vrátí hodnotu klíče "jmeno"
print(muj_slovnik.get("pohlavi", "Takový klíč není")) #vrátí hodnotu klíče "pohlaví", pokud takový klíč není, řekne "Takový klíč není"
print(muj_slovnik.pop("registrovany"))                #odstraní zadaný klíč a jeho hodnotu a vypíše tu hodnotu
print(muj_slovnik)                                    #hodnota/klíč odstraněn

#CVIČENÍ 1
print("="*15, "Cvičení 1 - Rozšiř slovník slovníkem", "="*15)
user_1 = {}
user_1["name"] = "Marek"
user_1["surname"] = "Parek"
user_email = "marek.parek@gmail.com"
user_1.update({"email" : user_email})
print("User #01", user_1)

#CVIČENÍ 2
print("="*15, "Cvičení 2 - Náhledy slovníků", "="*15)
employees = {
    "employee01" : {
        "name" : "Marek",
        "surname" : "Parek",
        "email" : "marek.parek@gmail.com"
    },
    "employee02" : {
        "name" : "Matous",
        "surname" : "Svatous",
        "email" : "matous.svatous@gmail.com"
    },
    "employee03" : {
        "name" : "anna",
        "surname" : "rana",
        "email" : "anna.rana@gmail.com"
    }
}
print("Všechny klíče:", employees.keys())
print("Všechny hodnoty:", employees.values())
print("Všechny údaje k poslednímu zaměstnanci:", employees["employee03"].items())

#CVIČENÍ 3
print("="*15, "Cvičení 3 - Slovník ve slovníku", "="*15)
id123 = {'jmeno': 'Thomas', 'vek': 45, 'zeme': 'Czechia', 'mesto': 'Brno'}
id124 = {'jmeno': 'Daniel', 'vek': 34, 'zeme': 'Czechia', 'mesto': 'Prague'}
id125 = {'jmeno': 'Eva', 'vek': 43, 'zeme': 'Czechia', 'mesto': 'Olomouc'}
databaze = {"id123": {}, "id124" : {}, "id125": {}}
databaze["id123"] = id123
databaze["id124"] = id124
databaze["id125"] = id125
print(databaze)

#CVIČENÍ 4
print("="*15, "Cvičení 4 - Ověření hesla", "="*15)
jmeno = "Marek"
heslo = "1234"
uzivatel = {"Marek" : "1234"}
if heslo == uzivatel[jmeno]:
    print("Ahoj", jmeno, "vítej v aplikaci! Pokračuj ...")
else:
    print("Uživatelské jméno nebo heslo nejsou v pořádku!")


print("="*15, "Sety (množiny)", "="*15)
#Sety (množiny)
set1 = {"žena", "růže", "píseň"}
print(set1)
print(type(set1))
prazdny_set = set()
print(type(prazdny_set))                 #tvorba prázdného setu
set_s_hodnotami = {"Michal", "Titl"}      #tvorba setu s hodnotami
print(set_s_hodnotami)
print(type(set_s_hodnotami))
muj_list = ["mesto", "more", "kure", "staveni"]
set_z_list = set(muj_list)                #vytvoření setu z existujícího listu
print(type(set_z_list))

print("="*15, "Metody setů", "="*15)
#ukázky metod setů
#sjednocení
set_a = {"zena", "ruze", "kost", "pisen", "Lucie", "Matous"}
set_b = {"zena", "ruze", "kost", "pisen", "Lukas"}
print(set_a.union(set_b))               # Alternativa: print(set_a | set_b)
#průnik
print(set_a.intersection(set_b))        # Alternativa: print(set_a & set_b)
#symetrický rozdíl asi aka disjunkce
print(set_a.symmetric_difference(set_b)) # Alternativa: print(set_a ^ set_b)
#rozdíl setu a a b - odečte od setu a set b
print(set_a.difference(set_b))           # Alternativa: print(set_a - set_b)
#přidávání a odebírání hodnot
set_a = {"zena", "ruze", "kost"}
set_a.add("pisen")                       #add pro přidání jedné hodnoty
set_a.update(("Michal", "Titl"))         #update pro více --> jsou KULATÉ ZÁVORKY DVAKRÁT!
print(set_a)
set_a.discard("Titl")                     #odstranění hodnoty
print(set_a)
set_a.pop()                               #pop metoda si vybere sama, co odstraní (!)
print(set_a)
print(set("hello"))                       #vytvoří set s UNIKÁTNÍMI hodnotami
print(set({'jméno':'John', 'přijmení': 'Smith'}))     #vytvoří set s unikátními klíči

print("="*15, "Frozen set" , "="*15)
#Frozen set
fs_set = frozenset("Michal")
print(fs_set)
print(type(fs_set))

#CVIČENÍ 5
print("="*15, "Cvičení 4 - Sjednocení setů", "="*15)