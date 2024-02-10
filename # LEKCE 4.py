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

#CVIČENÍ 5
print("="*15, "Cvičení 5 - Fizz Buzz", "="*15)
for cislo in range(0, 101):
    if cislo % 3 == 0 and cislo % 5 == 0:
        print("FizzBuzz")
    elif cislo % 3 == 0:
        print("Fizz")
    elif cislo % 5 == 0:
        print("Buzz")
    else:
        print(cislo)

#CVIČENÍ 6
print("="*15, "Cvičení 6 - Dělitel", "="*15)
vysledek = list()
start = 3
stop = 9
delitel = 3
if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int):
    for i in range(start, stop+1):
        if i % delitel == 0:
            vysledek.append(i)
        else:
            pass
    print(f"Zadaný rozsah: <{start}, {stop}>")
    print(f"Čísla dělitelná {delitel}: {vysledek}")
else:
    print("Zadané vstupy musí být čísla.")

#CVIČENÍ 7
print("="*15, "Cvičení 7 - Skript na seřazení", "="*15)
jmena = [
 'Michal', 'Pepa', 'Honza',
 'Pavel', 'Lukas', 'Matej',
 'Iva', 'Klara', 'Jana',
 'Honza', 'Vasek','Milan',
 'Michal'
]
kopie_jmen = jmena.copy()
print("TOHLE JSEM NEDAL :(((((")

#CVIČENÍ 8
print("="*15, "Cvičení 8 - Šachovnice", "="*15)
velikost = 20
sachovnice = []
symboly = ['#',' ']
for i in range(velikost):
    rada = list()
    index = i
    for j in range(velikost):
        if index in range(0, velikost, 2):
            if j % 2 == 0 or j == 0:
                rada.append(symboly[0])
            else:
                rada.append(symboly[1])
        elif index in range(1, velikost, 2):
            if j % 2 == 0 or j == 0:
                rada.append(symboly[1])
            else:
                rada.append(symboly[0])
    sachovnice.append(rada)
#    print(rada)
#print(sachovnice)
for i in range(len(sachovnice)):
    for j in range(len(sachovnice)):
        print(sachovnice[i][j], end="")
    print(" ")
#MÁM TO JINAK, NEŽ JE NABÍDNUTÉ ŘEŠENÍ, ALE FUNGUJE MI TO

print("#"*25, "DOMÁCÍ ÚKOL", "#"*25) #cílem je zjistit 3 nejčastější slova
text = """
Affronting imprudence do he he everything. Sex lasted dinner wanted indeed
wished out law. Far advanced settling say finished raillery. Offered
chiefly farther of my no colonel shyness. Such on help ye some door if in.
Laughter proposal laughing any son law consider. Needed except up piqued
an. Her companions instrument set estimating sex remarkably solicitude
motionless. Property men the why smallest graceful day insisted required.
Inquiry justice country old placing sitting any ten age. Looking venture
justice in evident in totally he do ability. Be is lose girl long of up give.
Trifling wondered unpacked ye at he. In household certainty an on tolerably
smallness difficult. Many no each like up be is next neat. Put not enjoyment
behaviour her supposing. At he pulled object others. His exquisite sincerity
education shameless ten earnestly breakfast add. So we me unknown as improve
hastily sitting forming. Especially favourable compliment but thoroughly
unreserved saw she themselves. Sufficient impossible him may ten insensible
put continuing. Oppose exeter income simple few joy cousin but twenty. Scale
began quiet up short wrong in in. Sportsmen shy forfeited engrossed may can.
Remain valley who mrs uneasy remove wooded him you. Her questions favourite
him concealed. We to wife face took he. The taste begin early old why since
dried can first. Prepared as or humoured formerly. Evil mrs true get post.
Express village evening prudent my as ye hundred forming. Thoughts she why not
directly reserved packages you. Winter an silent favour of am tended mutual.
Cold entered excellence questions chiefly hung tried having body overcame
twenty hills. Afraid easy admire settled promotion. Convinced full manners
household cottage savings giving sweetness. Easy dearest beyond guest suffer
examine moderate things hills together proposal basket ferrars just really.
Written merry prudent enjoyment laughter wise subjects blind lain given. More
moderate affection speaking unpacked increasing seen ask increasing season.
Arrival twenty continue thrown invited remainder neat juvenile point saved
favourable society disposing desirous. Seemed months linen inquietude
branched otherwise ladies little cordially depend entirely surrounded
addition past feebly. Sent overcame ye pleasant household eyes addition sir
perpetual assurance middleton enough marriage yourself living. Expenses times
inquiry he who thirty offended opinion removal stairs. Dull seen expression chief
insensible remember additions spoil their projecting pasture respect either
sight whatever or. Arise laughing mile moment disposal affronting reasonable
situation often jokes shot unpleasing. Wrong better those hopes man besides
must were although scale. Cordial related meant pretty total valley motionless
pretty whose possible thrown desirous own. Great without arranging room. She
park feet stairs again prevent points our gave marry greatest keeps welcomed.
Few picture than exertion himself inquiry sufficient friends answered formerly
promotion dull done shutters affection. Dining so china affixed followed
motionless surprise. Gentleman sing known hill age. Motionless paid hastened
sure enjoyment declared mistress. Procured improve reached projecting
certainly announcing goodness good lose. Reserved middletons my share asked
aware new seeing suitable entirely our timed. Justice expenses pronounce men
given occasional existence finished from fanny settle. Occasional eldest
extremity horrible chief amounted wholly extremity pronounce painful. Company
better every hastily held window. Dissimilar discretion pleased dashwood
children who branched. Settled on timed unpleasant prevent chiefly dinner. Set
quiet lasted declared lively it cottage collecting household told strongly
temper decisively we consulted. Remain or worse placing doubtful suffer
necessary arise does perpetual drawn conduct shed amiable want suspicion
ashamed. Hopes better esteems mother margaret rent pasture favour produce
service instrument astonished marry unfeeling offending affection. Ashamed
unleasing ourselves produce made entreaties suffering went express strongly
opinions year need burst away motionless jokes. Views securing furniture.
Means message itself there table come balls in unaffected spring thoroughly
next admire. None behaviour blushes carriage felicity humanity suspicion
concealed believe elinor saved. Sitting greater secure called replying
beauty sorry. Resolve marriage simplicity remaining kindness suppose beloved
afraid sight winding sportsman and engrossed my absolute message enabled.
Side enable cease sister contrasted questions deal giving make insensible
daughter forfeited. Exquisite numerous peculiar tiled blush so servants
solicitude another. Ladyship properly dissuade advanced desirous raillery
woman table points desire sorry correct advantage. Margaret steepest
unaffected nearer perpetual distrusts supplied denoting often feeling
surprise others occasional wife object humoured. Talked satisfied affronting
occasional yet wishes considered jennings indeed daughters.
Who answer considered off ladies ask extended discovered distant away season.
Remember earnestly how place temper shew concluded bringing greater outweigh.
Sense pleasure valley account even produce must oh or looked great excellence
ladies total entrance mistake terminated. Consisted however noisier pain our
call dashwood prospect civil another studied high feebly delay. Gravity
blessing defer county marriage. Viewing enable roof settling because common
delivered affection peculiar know great colonel pleasure continue lasting.
Written attacks humoured elegance passed branched estimating can. Certain
likewise reserved we situation. Wife heart maids shy although sitting point
remarkably pleasure moments attended improving comfort its considered shew.
Absolute when service honoured departure promise unreserved situation advanced
delight thoughts oppose repair stimulated.  Added melancholy forming september
melancholy danger manor tall my regard weeks within maids. Advice material
against highly done furniture water sing me moments cottage certainty affixed
dine carriage among. Entire besides raising advantages entreaties certainly
another. Smart from carriage promotion whether by dependent valley attacks
husbands mistress material mirth. Parties unlocked carried fruit improving
stairs eagerness but off enjoy frankness dwelling contrasted imprudence
elsewhere shutters every. Applauded vicinity every. Painful highly elinor.
Times could hastily contrasted ye. Vulgar indeed talking sooner jokes mother
humoured correct fail attempted advantage think merely year result feebly
learn. Length fifteen laughing shot remain welcome. Fancy unknown marked find
consider. Property express day then expense wish tears engaged called. Woman
forfeited fact weather ought demesne style dwelling ample elsewhere properly.
Total linen have forfeited. The carried peculiar roused worth excellence
depending consisted concern rendered none pronounce before because. Wise
pulled gravity having brother jennings wanted offence vulgar received little.
Nor would request miss announcing. Fortune inquietude past. Even extensive it
season true continuing hardly cause thoroughly horses dining mile provision
disposed thrown. Esteems juvenile nothing quitting mrs. Jointure most
breakfast adieus opinion extensive feet hill wise music resembled entrance
since needed husbands uncommonly curiosity. Civility though welcome winding
blind conveying lively spoil. Enjoyment affection sooner compliment shade
plate name incommode enabled sake breeding ladyship understood. Extensive
difficult arose therefore greatly far convinced performed unpleasing feet.
Made seems neglected early difficult years affixed. Ye hope or instrument
especially things distance colonel way. Chief admire wanted civility tried
gate compliment. Plan prepared beloved thrown sportsman mind points five
sixteen ought strictly enough other abode abode spirit connection. Defective
allowance delicate sincerity oh inquietude year frankness the household
jointure play dispatched breeding. Education pleasure fanny debating off
surrounded. Examine sportsman depending. Form true held help denote pasture
she. Marianne state supported elsewhere enjoyed abroad any pure. Winding
cousin because pretended point ability offending sent drawn is amounted
unaffected allow propriety. Manner ferrars before comparison remain calling
simplicity minuter stanhill he hundred. Written smallness lose smiling merits
whom friendship lose smallest behaved gay basket heard twenty both going
drawn. Her morning left. Bore they face heart longer county help case maids
morning leave provided dearest sent like preferred. Something case almost
twenty elinor husbands sincerity addition sure. Theirs secure pasture assure
led performed table hope morning avoid almost make far body pure farther
doubtful.  Exquisite horrible admire six know. Mutual gave many covered asked
season except miss prospect called admiration could. Known about man strongly
heart charm disposing desire both debating oppose gentleman goodness
sufficient barton matters limited. Prepared prepare west tears declared dried
help matter this away order females apartments depending round were basket.
"""
#cílem je zjistit 3 nejčastější slova
vycistena_slova = list()
for i in text.split():
    vycistena_slova.append(i.strip(",.;").lower())
vyskyt_slov = {}
for i in vycistena_slova:
    vyskyt_slov[i] = vycistena_slova.count(i)
tri_nejcastejsi = sorted(list(vyskyt_slov.values()), reverse=True)[:3]
print(tri_nejcastejsi)
for i in vyskyt_slov:
    if vyskyt_slov[i] in tri_nejcastejsi:
        print(vyskyt_slov[i], i)

print("&"*25, "UDĚLAT PRVNÍ PROJEKT V PYTHONU", "&"*25)