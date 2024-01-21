# LEKCE 1
print("helo, this is the first ever print of this course")

print(type(5)) #int
print(type("text")) #str
print(type(5.5)) #float

print(10 / 3) #dělení na desetinná
print(10 // 3) #dělení (zahodím zbytek)
print(10 // 4)
print(10 % 3) #fce modulo (vrátí zbytek --> dobré na cyklování)
print (11 % 3)
print(2 ** 2) #umocňování
print(2 ** 3)

print(type("ahoj"))
print("he said \"helo\"!") #zpětné lomítko před uvozovkami ve stringu, aby printnul uvzovky
print("\n helo \t helo") #příklad special znaků pro odskakování apod.

print(2+2) #4
print("2"+"2") #22
print(2.0+2) #4.0

print(type(float(2))) #float
print(float(2)) #2.0
print(type(int(2.0))) #int
print(int(2.0)) #2
print(2 + float("2")) #4.0

print("nakoupil jsem " + str(10) + " kusu")
#práce se stringem
print("Michal " + "Titl")
print("Michal" + " " + "TITL") #spojí dohromady
print(10 * "X") #je to fajn na vizuální oddělování
print("Miata " * 3) #napíše xkrát
print(10 * "X")
print("Michal"[0]) #indexování (první prvek 0, poslední = počet písmen -1)
print("michal"[-1]) #lze i od konce, ale tam se začíná od nuly
print("michal"[-2])
print("michal"[-3])
print("michal"[-4])
print("michal"[-5])
print("michal"[-6])
print("michal titl"[0:6]) #slicing --> michal
print("michal titl"[5:]) #když neuvedu druhý parametr --> bere jako do konce
print("X" * 10)
print("0123456789"[0::2]) #striding - když chci třeba každé druhé číslo
print("0123456789"[10::-2]) #minusové znaménko --> jde od konce
print("\n XXX XXX XXX" * 3)

################
jmeno = "Michal"
vek = "23"
print(jmeno, vek)

jmeno1 = "Michal" "Titl"
print(jmeno1)

seznam = ["první", "druhy", "treti"] #list
print(seznam)
print(seznam [0:2])
print(seznam [1])
seznam [1] = "xty" #LZE měnit hodnoty
print(seznam)

seznam1 = [["prvni", "druhy", "treti"], [ "CTVRTY", "PATY"]] #tuple
print(seznam1[0:1])
print(seznam1[0:2])
print(seznam1[0:1], seznam1[1:2])
print(seznam1[1:2])
print(type(seznam1))
print(type(tuple(seznam1)))

#ZKOUŠENÍ UČIVA DLE PORTÁLU
#cvičení k rozdělení stringu
print("\n")
print("Prvních 5 písmen:")
print("indexování"[:5])
print("Posledních 5 písmen:")
print("indexování"[5:])
print("Každé 3. písmeno (počínaje prvním) od 'i':")
print("indexování"[::3])

#proměnné
mojeJmeno = "michal"
jmeno1 = "misa"
moje_jmeno_1 = "michnik"
print(mojeJmeno, jmeno1, moje_jmeno_1)
PI = 3.14
print(PI) #pokud se jmeno proměnné neměnní --> jméno VELKÝMI PÍSMENY
pet = 5
sest = 6
print(pet + sest)

#sekvenční datové typy - list, tuple, range (list, n-tice, rozsah)
IDs = (["Michal", "Titl", "Brno"])
print(IDs)
print(type(IDs))
    #jak vytvořit list
print("\n")
seznam1 = []
seznam2 = list()
print(type(seznam1))
print(type(seznam2))
seznam3 = [2, 4, 6, 8, 10]
seznam4 = [1.0, 3.0, 5.0, 7.0, 9.0]
print(seznam3)
print(seznam4)
print(seznam3[0])
print(seznam3[2])
print(seznam3[-1])
    #tuple - kulaté závorky, NENÍ změnitelný (asi není gut tvořit prázdné)
mesta_CR = ("Praha", "Brno", "Ostrava", "Plzen")
print(mesta_CR)
print(type(mesta_CR))
tupl1 = ()
tupl2 = tuple()
print(type(tupl1))
print(type(tupl2))
tupl3 = 1.3, 3.6, 1.8, 0.4, 1.9 #tuple lze vytvořit i BEZ ZÁVOREK
print(type(tupl3))
print(tupl3)
print(mesta_CR[0])
print(mesta_CR[-1])
print(mesta_CR[0::2])

#zabudované funkce
print("\n")
type("123") #nic tam není, protože sice se něco stane (označí typ), ale nechceme po něm vypsání
print(type("123"))
print(type(3.14))
print(type(["m", "h"]))
muj_typ = type("X")
print(muj_typ)
delka = len("delka")
print(delka)
print(float(delka))
print(max(seznam4))
print(sum(seznam4))
vek = "skoro 24"
print("Jmenuji se " + mojeJmeno + " .Je mi " + vek + " let.")
# print(help(print))
print(round(0.25, 1)) #zaokrouhlí na 1 desetinné místo
print(round(0.25, 3)) #zaokrouhlí na 1 desetinné místo
print(abs(-1)) #vrátí absolutní hodnotu
print(abs(125)) #vrátí absolutní hodnotu
print(int(3.14)) #převede float na int
print(int("11")) #převede string na int
print(float(12)) #převede int na float
print(float("12")) #převede string na float
print(float("1.12")) #převede string na float
print("Těch funkcí je spousty - třeba takhle lze dělat z listu tuple a naopak, sečíst znaky, hledat maxima, minima, sumovat, ...")
vstup = input("zadej cislo: ") #input(text co vidí user)
print("zadane cislo je", vstup)
print(type(vstup)) #výstup je VŽDY string, pokud neřeknu jinkak
vstup1 = int(input("dej cislo: "))
print(type(vstup1))
print(pow(3, 2)) #3 na druhou
print(pow(10, 3)) #10 na třetí
print("#" * 20)

#cvicení převadeč jednotek
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26
kg_pocet = 80
km_pocet = 54
l_pocet = 5
kg_vysledek =  kg_pocet * kg_lb
km_vysledek = km_pocet * km_mile
l_vysledek = l_pocet * l_gal
print(kg_pocet, "kg je", kg_vysledek, "lb")
print(km_pocet, "km je", km_vysledek, "mil")
print(l_pocet, "l je", l_vysledek, "gal")

#cviceni nakupujeme auto
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva_merc = 5000
cena_2_merc = 2 * mercedes
cena_merc_a_rolls = mercedes + rolls_royce
cena_2_rolls_s_vybavou = 2 * (rolls_royce + vybava)
cena_merc_s_vybavou = mercedes + vybava
merc_se_slevou = mercedes - 5000
print("Sleva na Mercedes:", sleva_merc)
print("Cena za dva Mercedesy je:", cena_2_merc)
print("Cena za Mercedes a Rolls-Royce:", cena_merc_a_rolls)
print("Cena za dva Rolls-Royce s příplatkovou výbavou:", cena_2_rolls_s_vybavou)
print("Cena za Mercedes s příplatkovou výbavou:", cena_merc_s_vybavou)
print("Cena za Mercedes po slevě:", merc_se_slevou)

#cviceni spojovani stringu
jmeno = "Lukáš"
prijmeni = "Dvořák"
cele_jmeno = jmeno + " " + prijmeni
delka_jmena = len(cele_jmeno)
print("Celé jméno:", cele_jmeno)
print("Délka jména:", delka_jmena)
print("=" * delka_jmena)
print(cele_jmeno)
print("=" * delka_jmena)

#ukol z lekce 1 - uživatel zadá město z nabídky a dostane cenu spojení
mesta = [ "Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
nabidka = "\n1 - Praha - 150 \n2 - Viden - 200\n3 - Olomouc - 120\n4 - Svitavy - 120\n5 - Zlin - 100\n6 - Ostrava - 180"
oddelovac = "#" * 30
print("\n", oddelovac, 
      "\nKam si přejete cestovat?", 
      "\n",
      "\nMožnosti jsou:", nabidka)
print(oddelovac)
cil = int(input("Jaké číslo má město, kam chcete jet?  "))
print(oddelovac)
print("Cena jízdného do města jménem ", mesta[cil-1], " je ", ceny[cil-1], " korun českých.")

#zkusím se inspirovat řešením lektora
mesta = [ "Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
nabidka = """1 - Praha   - 150 
2 - Viden   - 200
3 - Olomouc - 120
4 - Svitavy - 120
5 - Zlin    - 100
6 - Ostrava - 180"""            #očivindě když tam dám ty trojité uvozovky, tak to můžu skládat do další řádků
oddelovac = "=" * 30
print(
    "VÍTEJTE V NAŠÍ NABÍDCE",
      oddelovac,
      nabidka,
      oddelovac,
      sep = "\n"         #sep= je argument pro nastavení oddělovače
)
cil_cesty = input("Cílové město: ")
print(oddelovac)

index_mesta = mesta.index(cil_cesty)     #list.index(prvek) najde a vrátí pozici prvku v listu !!!
cena = ceny[index_mesta]
print("Cena jízdného do města ", mesta[index_mesta], " je ", cena, " korun českých.")
print(oddelovac)