<h1> Poznámky ke kurzu </h1>

<h2> ÚVOD - 17.1.2024 </h2>
- z každé lekce nahrávky na engeto platformě
- dole pod hodinami/projekty jsou odevzdávárny
- čas na certifikaci až 10 měsíců - do 17.11.2024
- kariérní poradenství až od 2. 1/2 kurzu, resp až budeme ready (latest 17.11.2024)

**operations poznámky k úvodu**
- od lektora (Petr Lorenc)
- na začátku opakování z minule (10 minut)
- pak vždy 3x (45min nová látka, 5min úkol, 10min pauza)
- v úkolech se snaží spíš kritizovat, ať máme na čem stavět (pochvala je fajn, ale tolik neposune)
- PDF Jupyternotebooků bude u lekcí na platformě jako odkaz na Gdrive

<h2> LEKCE 1 - ÚVOD DO PROGRAMOVÁNÍ </h2>

- dneska už jsme na dost vysoké úrovni abstrakce --> nemusíme psát v binárním kódu, ale počítač tomu rozumí i tak (X začátky)
- repetitivní a nekreativní úkoly je dobré nechat počítači --> programování
- python (a třeba SQL) je fajn čitelný ze startu X třeba Céčko už tolik ne (ale zase pak je Céčko rychlejší) X assembler (téměř to nejnižší)
- plus taky v Céčku třeba musím program prvně kompilovat X Python je o řád jednodušší (stačí uložit a pustit)
- C je old, ale Python už má taky 32+ y.o. --> prověřen časem
- btw Kotlin je podobnej Python, jen běží na Jave
- jak zjistit verzi Pythonu? ___ python --version
- v prezentaci *zajímavé* odkazy na obsah instalace Python - např. compiler
- interpreter - vezme source file, zkompiluje do byte codu, pošle do virtual machine a pustí se program
- lze psát program hned do konzole, ale je nutné to mít rozmylšený dopředu, protože program je basically jen postup kroků (takže bych ty kroky musel skládat správně a neudělat v procesu chybu - nemůžu tam skákat)
- krom konzole, notepadu, IDEs, ..., lze používat i notebooky - např. jupyternotebook (lokální), Colab od Googlu (web) ad. - interaktivnost konzole, jednoduchost editoru a pomáhá psát jak IDE
- každý má svoje specifika: třeba notebooky mohou rovnout importovat knihovny, ale zase mají specifické funkce občas, jupyternotebooky háže výsledky hned pod to (takže u *datové analýzy je to hooodně common!*)
- syntaxe = jak položíme ty slova za sebe X sémantika = co tím chci říct

<h3> Syntax </h3>

- patří sem ty fce, podmínky, smyčky, ...
- Python zarovnává do bloků (viz PEP 8)

<h3> Číselné hodnoty/datové typy </h3>

= kufříky, které mají nějaký tvar, který se liší dle toho, co do něj vkládáme
- python umožňuje do tohoto kufříku dávat čísla i řetězce (líp se píše, hůř identifikuje chyba) --> použití fce type()
- int() jako celá čísla; float() jako desetinná
- klasické operátory; navíc to dělení na desetinná čísla / a celá // a modulo % (tj. zbytek po dělení)
- problém s float (viz platforma, že 0.1+0.2 se nerovná přesně 0.3), řešitelné knihovnou decimal
- operátory mají nějaké pořadí: jako v matice, ale násobení je před dělením a sčítání před odčítáním, násobení před dělením
- v Pythonu je dobré být explictní, než implicitní = používat závorky, jak se má, neházet je zbytečně apod.
- python nechce ztrácet přesnost --> operace int a float má za výsledek float
- lze přetypovat pomocí stejnojmenných fcí

<h3> Textové hodnoty </h3>

= kufřík na znaky
- str() jako řetězec
- můžu tam hodit v podstatě jakýkoliv znak, ALE pak už NELZE měnit!
- 4 způsoby jak napsat string: 1 nebo 3 na začátku a konci + jednoduché nebo dvojité uvozovky
- když chci použít uvozovky v tom výsledku, tak: 
    1) použít druhý druh uvozovek
    2) přidat před uvozovku zpětné lomítko \
- máme nějaký special znaky a písmenka (pro nový řádek, tabulátor apod)
- lze taky sčítat, ale zřetězí je to
- NEchceme míchat datové typy (!)
- desetinná je v Python tečka, ne čárka

<h3> Zabudované funkce </h3>

- print
- help (podobněj jako dir --> help(nazev objektu))
- dir (to je dobrý, když dám jako print(dir(nazev objektu), tak mi to hodí možnosti, co s tím dělat))
- input
- ... a další

<h3> Možnosti formátování stringu </h3>

- spojování, opakování, indexování, slicing, striding + další
- indexování: print("Text"[parametr])
- odpředu od 0 po počet znaků minus 1
- odzadu se začíná -1 do -1 minus počet znaku
- slicing: print("text"[parametr:parametr])
- počítání jak u indexování, ale místo výběru vysekávám výsek --> [0:4] budou znaky na pozici 0, 1, 2, 3, 4; klidně může být třeba [5:10] nebo [5:] --> to bude od 5. pozice do konce
- striding: nechceme každý číslo ve výběru, ale třeba každý druhý --> např. [1:8:2] = od 1. do 8. pozice, každá 2. pozice
- když se dá ve stridingu negativní číslo --> jde se od konce
- ... obecně první číslo = kde začnu; druhé číslo = kde končím; třetí číslo = jak procházím string

<h3> Proměnná </h3>

= vlastně ten kufřík (ne jeho tvar)
- takže třeba jako:

jmeno = "Michal"

vek = "23"

print(jmeno, vek)
- lze pouzit různé názvy, ALE nesmí začínat číslem, krom podtržítka žádné special znaky, nesmí mít mezery + je SILNĚ doporučeno se vyhnout názvům už built-in (např. str, int, float, print apod.) klíčový slova (!)
- plus viz taky tipy v PEP8: např. nepoužívat samotné lko (ještě v combu s Ičkem), velké O (zaměnitelné s 0) atd.

<h3> Řetězce a tuples </h3>

- datové typy s více hodnotami - sekvenční datové typy (seznam, ntice, rozsah) (list, tuple, range)
- plus tam funguje zase striding, indexing, slicing a taaaak
- list = sekvenční datový typ - definovaný [], oddělujeme prvky čárkou, lze měnit obsah
- lze měnit hodnoty: nazev_list[misto v listu] = "novy prvek"
- tuple = podobný jak seznam, ale NEmůžu tam měnit hodnoty
- plus musíme explicitně říct, že chceme dělat tuple --> type(tuple("a"))
- POZOR: listy/tuples lze vnořovat --> takže když budu mít třeba seznam = [[0], [1]], ... DOPLNIT Z ODPOVÍDAJÍCÍHO JUPYTERU

***ÚKOL DO PŘÍSTĚ NA VYZKOUŠENÍ V JUPYTERU - hotovo, viz soubor s kódem***

<h2> LEKCE 2 - Podmínky a metody (24.1.2024) </h2>

<h3> opakování z minula </h3>

- trojité uvozovky odpovídají vícřádkovému zápisu; třeba místo \n text \n
- objekt[:] = objekt [::]
- objekt[::-2] --> každý druhý ale od konce
- objekt[::-1] --> každý první od konce --> pozpátku
- krom objektu/řetezce tam může být list i ten tupl žejo
- POZOR NA TOTO: 
-   "Lorem imsum dolor sit amet"[0:5:-2] = [] protože už [0] je to méně než zarážka 5
-   "Lorem imsum dolor sit amet"[5:0:-2] = [5, 5-2, 5-4] ale už ne [5-6] protože je to méně než zarážka 0
- POZOR taky na tvorbu kopií objektů ve stylu pole = kopie --> když změním jedno, změní se zbytek --> lepší pole = kopie.copy()

<h3> Boolean </h3>

- pro řešení podmínek, je potřeba znát boolean
- příp. bool
- o pravdivosti (TRUE X FALSE)
-   true je basically 1, false 0 --> boolean je basically special case integer (tj. taky datový typ)
- funkce bool jako rozhodčí --> print(bool(....)), i když to bool tam být asi nemusí, záleží prý
- plus de facto převádí 1 a 0 na True nebo False, resp 0 --> False, vše co není 0 --> True

<h4> Srovnávání </h4>

- často u těch booleanů
- > < >= <= == (rovná se) != (nerovná se) is (je totožné) is not (různá objektová identita)
- (!) == rovná se se používá pro testování rovnosti X = rovná se se používá k přiřazování hodnot

<h4> Objekty/id </h4>

- všechno je objekt v Pythonu
- --> vše má své označení (lze zjistit pomocí fce id)
-   identické hodnoty = stejné číslo, tedy adresu objektu v paměti PC
-   platí to i pro proměnné, které vznikly spolu: např. promenna1 = "Holinka" promenna2 = "Holinka" --> promenna1 == promenna2 bude True
-   ALE pokud budou na začáku jiné a pak se změní, aby byl stejné, tak je *třeba použít == místo is, aby to řešilo obsah, ne adresu!*
- *--> is řeší adresu, == řeší obsah*

<h4> Operátory </h4>

- mají své operátory: and, or not
-   and: např. True and True (výsledek True) ... jakmile by viděl False --> výsledek False
-   plus *zkrácené vyhodnocení* - vidí False a na další se už ani nepodívá
-   or: stačí jeden True a je to celé True
-   not: dává se jednomu objektu a obrací hodnotu True --> False NEBO False --> True
- *pořadí vyhodnocování*: not --> and --> or (ALE na hodině říkali z leva do prava?!?!?!?!)

<h4> Zkrácené vyhodnocení </h4>

- u or jakmile bude to první True, tak se to vezme
- u and si tím ušetřím zase psaní kódu - nejčastěji se používá u prvků z polí (listů/tuplů)
- asi to není tak důležitý, ale měl bych si to checknout

<h4> Ověřování členství </h4>

-   zda je něco v něčem - např. ("M" in "Michal"), nebo není --> ("M" not in "Brno") ... oboje True
-   používá se k tomu in, popřípadě not in
-   testuje přesnou shodu ("m" in "Michal" bude False)
-   btw stejná skupina funkce jako slicing, indexing, striding, ...

<h4> Vyhodnocování booleanů </h4>

- *vyhodnocování* (když je tam fce bool předtím) probíhá dle toho převodu True na 1 a False 0
-   --> např. True + False = True, protože 1 + 0 = 1
-   --> např. True - False = True, protože 1 - 0 = 1
-   --> POZOR že když není tam to bool, tak to převede a např. True + True nebude True ale 2 (!)
- bool stringů --> bool("a"), bool("0"), bool(" ") ... všecno je true, protože je nenulový (ale bool("") už bude False)
- None = absence hodnoty (není to definované, chybí, ..., jinde aka Null, NaN apod.)
-   např. seznam = [] není to stejné jako seznam = None (!!!)

<h3> Podmínky </h3>

<h4> Jednoduchý podmínkový zápis </h4>

- rozhodování pomocí boolean hodnot --> je či není pravdivý
- potřeba podmínkového zápisu: if něco je TRUE: má se stát (např. if jmeno == "Michal":    print("Ahoj, Michale"))
- musí tam být to if, dvojtečka i odsazení za dvojtečkou na novém řádku
- to odsazení je důležitý, je to součást syntaxu, bez toho se to rozpadne a hodí error
- když je to FALSE --> nic se nestane (z toho odsazeného
- if lze kombinovat s else --> za konec původního přidám else: print("Ahoj, ostatní))
- else se aktivuje, když je podmínka FALSE
- jde to kombinovat do více vrstev, např.: 
if 
____if
____else
else
____if
________if
________else
____else

- POZOR na víc if po sobě --> když bude platit jedno i druhý (případě prostě ty další), tak se vykonají všechny (!)

<h4> Rozvinutý podmínkový zápis </h4>

- if/elif/else --> když chci 3 a víc větví, kterými se lze vydat
- elif je kombo obojího: dává se tam podmínka, co má být TRUE, a výsledek, když bude TRUE + nastává, když if není TRUE
- ale elif může být kolik chci (!)
- pořadí: if - elif - ... - else
- elif se spustí, když je if FALSE --> další elif nebo else se už nevykoná (kdežto další if by se vykonalo, pokud by platilo)
- prostě v tom chainu if - elif - ... - else jakmile dojde k pravdě, tak se vykoná a další se už neřeší
- podmínky lze samozřejmě doplňovat o boolean operátory: and, or, not
- každopádně to musí být TRUE, aby se spustil odpovídající příkaz --> platí výsledky kombinací True a False dle výše

<h4> Ternární operátor </h4>

- existuje nějako ternární operátor: alternativní způsob zápisu podmínky buď anebo ---> X if Y else Z
- např.
jmeno == "Michal"
print("Ahoj, Michale) if jmeno == "Michal" else print("ahoj, ostatni)
- je to asi úspornější na řádky (klasická alternativa výše popsaného by měla 5 řádků místo 2), ale na komplikované věci to bude asi nepřehledné
- plus možná je to logičtější ("vytiskni Ahoj Michale, pokud je jméno Michal, jinak ... X pokud je jméno michal, vytiskni ..., jinak, ...)
- můžu ale používat to "klasické"

<h3> Metody </h3>

- = jakoby fce zaměřené na konkrétní datový typ (str, list apod.) X fce jsou sdílené mezi datovými typy
- např. pro print stringů: print("michal".upper()) --> vše caps lockem
- --> zápis je: objekt.metoda(argumenty)
- --> MUSÍ se to volat na nějaký OBJEKT
- je jich spousty (pro stringy): capitalize, casefold, center, count, find, format, isalnum, isaplha, isdigit, join, ljust, replace, split, zfill)
- ale i pro listy: append, clear, copy, copy, count, extend, index, insert, pop, remove, reverse, sort
- u tuplů možná míň: count, index
- nic z těch výpisů není ale vyčerpávající asi
- můžu si je všechny zavolat např. skrze help(datovy_typ), print(dir(str)) nebo OBECNĚ help(datovy_typ.nazev_metody) ... nebo místo str dát list, tuple, int, ... každý datový typ má své metody
- obecně je dobré si to projít skrz ten help

***V JUPYTERU JE ÚKOL NA ROZLOUČENOU (co má/nemá heslo obsahovat) - DONE***

<h2> LEKCE 3 - Slovníky a množiny (31.1.2024) </h2>

<h3> opakování z minula </h3>

#N/A

<h3> Slovníky </h3>

- datový typ tvořen počtem párů dat
- pár = "jméno klíče" : jeho hodnota
- klíče jsou stringy, hodnoty různé, musí být zapsaný jako nezměnitelné (nemůže to být tuple nebo druhý slovník...jako hodnota ale jo)
- lze vytvořit i prádzný
- lze vytvořit pomocí nazev = {obsah} i pomocí nazev = dict(obsah)
- hledání hodnot ve slovníku = mapování
- podobné jak indexování (dáváme do hranatý závorek klíč), ale není tam to pořadí (např. print(slovnik["nazev_klice"]))
- klíče musí být unikátní, jinak se přepíšou
- jak vložit klíče/hodnoty? dám nazev_slovniku["nazev_klice"] = "hodnota"
- lze vkládat slovníky do slovníků: vytvořím např. slovník kontakty s nějakým obsahem a pak do např. slovníku info uložím jako info["kontakt"] = kontakty
- tomu se říká nestování; volám to pak podobně: např. print(info["kontakty"]["telefon"])

<h3> Metody slovníků </h3>

- jako ostatní datové typy i slovníky je mají
- např. clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values

<h3> Sety (množiny) </h3>

- 