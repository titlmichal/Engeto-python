# LEKCE 3
nazev_lekce = "LEKCE 3"
delka_nazvu_lekce = len(nazev_lekce)
print("="*15, nazev_lekce, "="*15)
print("-" * (30 + delka_nazvu_lekce + 2),)

print("="*15, "Úkol na rozcvičení", "="*15)
usernames = ["Petr", "Jan", "Pavel", "Kristyna", "Helena"]
passwords = ["Heslo1", "Heslo2", "Heslo3", "Heslo4", "Heslo5"]
cities = ['Brno', 'Plzeň', 'Olomouc', 'Liberec', 'České Budějovice', 'Hradec Králové', 'Ústí nad Labem', 'Pardubice', 
          'Zlín', 'Ostrava', 'Karlovy Vary', 'Jihlava', 'Praha', 'Paskov', 'Kladno']
distances = [
[0, 296, 77, 307, 216, 168, 296, 146, 96, 169, 337, 93, 208, 176, 240],
[296, 0, 369, 200, 137, 208, 181, 213, 388, 462, 81, 217, 92, 469, 100],
[77, 370, 0, 236, 290, 139, 370, 135, 63, 98, 411, 167, 282, 104, 314],
[309, 198, 237, 0, 249, 98, 96, 155, 401, 434, 233, 230, 110, 449, 135],
[217, 137, 290, 250, 0, 253, 239, 258, 309, 383, 218, 138, 151, 389, 183],
[167, 209, 140, 97, 253, 0, 190, 24, 206, 238, 240, 112, 116, 245, 143],
[298, 181, 371, 96, 238, 190, 0, 196, 390, 463, 122, 219, 93, 470, 87],
[146, 214, 135, 154, 193, 24, 196, 0, 201, 234, 246, 90, 121, 240, 149],
[96, 389, 62, 400, 308, 206, 389, 202, 0, 124, 430, 186, 300, 131, 333],
[170, 463, 94, 440, 383, 239, 463, 235, 125, 0, 504, 261, 375, 14, 407],
[337, 82, 410, 234, 218, 241, 121, 246, 429, 502, 0, 258, 127, 509, 105],
[93, 218, 167, 229, 138, 113, 218, 90, 186, 259, 259, 0, 130, 266, 162],
[209, 91, 282, 109, 150, 116, 92, 121, 301, 375, 128, 130, 0, 382, 31],
[176, 469, 100, 451, 388, 244, 469, 240, 131, 13, 510, 266, 380, 0, 412],
[240, 99, 313, 135, 181, 143, 86, 148, 332, 406, 105, 161, 31, 412, 0]
]
#pozdravit uživatele --> přihlášení dle jména a hesla --> (vypsat města) --> zadat místo A B --> vypíše vzdálenost mezi městy
print("X" * 10, "Vítej v systému vzdálenosti", "X" * 10)
jmeno = input("Zadej uživatelské jméno: ")
heslo = input("Zadej heslo: ")
if jmeno in usernames:
    index_hesla = usernames.index(jmeno)
    if heslo == passwords[index_hesla]:
        print("Jméno a heslo je správné")
        print("Máte na výběr z těchto měst, kam můžete cestovat:", cities)
        misto_A = input("Zadejte město, ze kterého budete cestovat: ")
        misto_B = input("Zadejte město, do kterého budete cestovat: ")
        if misto_A in cities and misto_B in cities:
            index_mesta_A = cities.index(misto_A)
            index_mesta_B = cities.index(misto_B)
            if index_mesta_A == index_mesta_B:
                print("Nemůžete cestovat na a do stejného místa!")
            else:
                print("Vzdálenost z místa", misto_A, "do místa", misto_B, "je", distances[index_mesta_A][index_mesta_B], "km.")
        else:
            print("Zadaná města jsou špatně")
    else:
        print("Heslo není správné")
else:
    print("Jméno je špatně")


print("="*15, "Slovníky", "="*15)
#slovníky
muj_slovnik = {
    "jmeno": "Michal", 
    "registrovany": True, 
    "vek": 24
        }
print(muj_slovnik)
print(type(muj_slovnik))
prazdny_slovnik = {}
print(type(prazdny_slovnik))
slovnik_skrze_fci = dict(jmeno = "Michal", vek = 25) #zde KLASICKÉ ZÁVORKY! když je to skrz fci --> omezí se tím množství možností, co může být klíč
print(slovnik_skrze_fci)
slovnik_o_Mazde = {
    "make" : "Mazda",
    "model" : "MX-5",
    "year" : "1999",
    "colour" : "brilliant black",
    "engine" : {
        "displacement" : 1800,
        "gearbox" : "manual",
        "odo" : 185_000,                        #skrze ty podtržítka je možné psát dlouhá čísla a oddělovat je pro přehlednost
    },
    "state" : {
        "rust" : "not much",
        "oil leaks" : "not really",
        "factory" : "definitelly not",          #tady je dobrý dát čárku, i když je poslední, aby pak další člověk tam neudělal omylem chybu, až to otevře
    },
}
print(slovnik_o_Mazde)
print(slovnik_o_Mazde["model"])
print(slovnik_o_Mazde["engine"]["gearbox"])
print(slovnik_o_Mazde["engine"]["odo"])
print(slovnik_o_Mazde["state"]["rust"])

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
print("="*15, "Cvičení 5 - Sjednocení setů", "="*15)
cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)
sjednocene_hodnoty = set(cisla_1).union(set(cisla_2))
print("Sjednocené hodnoty ze zadání:", sjednocene_hodnoty)

#CVIČENÍ 6
print("="*15, "Cvičení 6 - Rozdíl setů", "="*15)
cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}
rozdil_cisel = cisla_1.difference(cisla_2)
print("Rozdílné hodnoty prvního setu oproti druhému:", rozdil_cisel)