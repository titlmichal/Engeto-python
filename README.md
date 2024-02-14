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

- btw jak dostat help z konzole?
- zapnu python
- a dir(help) pro široký help
- dir(nazev_objektu) pro možné fce/metody --> zajimá mě to BEZ PODTRŽÍTEK
- nebo help(nazev_objektu) pro širší/detailnější výpis
- a pak dak třeba help(nazev_objektu.nazev_metody) pro detail

- btw2 - test driven development
- basically si ještě před psaním kódu nadefinuju cíle/pravidla a napíšu si pro to podmínky

- btw rozdíl == a is
- == řeší obsah
- is řeší i id
- takže asi lepší to == (minimálně u těch slovníků)

- btw fce .strip() - např. string_se_jmenem.strip() --> odmaže mezery na začátku a konci --> hodí se to na kontrolu hesel apod.
- btw něco zasapný velkým písmem by se mělo brát jako konstanta a neměli bychom to měnit

<h3> opakování z minula </h3>

- v materiálech je zajímavý odkaz na StackOverflow, kde je vysvětlený aplikovaný rozdíl mezi isdecimal(), isnumber() a isdigital()
- bool(True + True + True) = 3 ale bool(True and True and True) = True

***V JUPYTERU JE ÚKOL NA ROZCVIČENÍ - UDĚLAT***

<h3> Slovníky </h3>

- datový typ tvořen počtem párů dat (není třeba definovat, je built-in) --> nemusíme řešit, která informace je na které pozici
- pár = "jméno klíče" : jeho hodnota
- *(!) nejsou tam indexy* --> nutné dohledávat skrze klíče, ne indexy (jako u tuplů a listů, pokud nějaké to číslo není klíčem)
- *(!) nemají pořadí*, jakkoliv se to při definování zdá
- *(!) je změnitelný*
- klíče jsou *neměnné datové* typy (string, int, tuple apod.) - lze ověřit pomocí pokusu o jeho změnu (při pokusu o změnu chyba --> neměnný --> může být jako klíč), případně skrze fci hash() --> když vrátí číslo a ne chybu --> gut
- lze vytvořit i prázdný (slovnik = {})
- lze vytvořit pomocí nazev = {obsah} i pomocí nazev = dict(obsah)
- hledání hodnot ve slovníku = mapování
- *podobné jak indexování* (dáváme do hranatých závorek klíč), ale není tam to pořadí (např. print(slovnik["nazev_klice"]))
- plus oproti indexování nelze jít zpět (od hodnoty ke klíči)
- klíče musí být *unikátní*, jinak se přepíšou (a vypíše se pak ten poslední)
- hodnoty mohou být de facto cokoliv ... i třeba další slovník (viz nestování níže)
- jak vložit klíče/hodnoty? dám nazev_slovniku["nazev_klice"] = "hodnota"
- lze vkládat slovníky do slovníků: vytvořím např. slovník kontakty s nějakým obsahem a pak do např. slovníku info uložím jako info["kontakt"] = kontakty
- tomu se říká nestování; volám to pak podobně: např. print(info["kontakty"]["telefon"])
- btw nestovaný slovník může mít klíč z hlavního slovníku (stačí, aby byl unikátní v rámci souboru klíčů hlavního slovníku)
- v praxi se prý často používají slovníky na kódování slov na čísla (nebo naopak)
- v praxi taky *requesty chodí jako slovníky - jsou to JSON soubory, které to hážou do slovníků*
- --> vedle řetězce nejdůležitější datový typ

<h3> Metody slovníků </h3>

- jako ostatní datové typy i slovníky je mají
- např. clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values
- *copy dělá mělkou kopii* --> když tam pak přepisujeme data u zanořený slovníků, tak to udělá u obou --> je třeba udělat kopii hlavního i vnořeného
- slovnik.keys() --> vrací objekt se všemi definovanými klíči ve slovníku
- slovnik.values() --> podobný ale pro hodnoty
- slovnik.items() --> kombinace obou (taky vrací v párech, hodí se to na práci s cykly)
- ale (aspoň u těhle) tyhle metody dávají výstup, kteří předchazí např. dict_items a hlavně tam *NEFUNGUJE INDEXOVÁNÍ* --> řeší se to přetypováním na list
- slovnik.get("hledany_klic") --> vrací hodnoty daného klíče, pokud nenajde, tak None nebo to, co si definujeme za čárkou, např. ..get("klic", "není tam")
- slovnik.clear() --> vymaže celý slovník
- dict(zip(list1, list2)) --> vytvoří *z 2 listů 1 slovník*

<h3> Sety (množiny) </h3>

- na první pohled podobný slovníku, ale prakticky jiný
- u slovníků hledání hodnot skrze klíče, u setů hlavně množinové operace (neřeší tolik hodnoty uvnitř)
- --> na první pohled {} neznamená slovník, rozdíl *je v absenci těch vztahů klíč-hodnota a teda i těch dvojteček*
- hlavně se hodí na vyhledávání (oproti třeba listům - protože sety/množiny jsou asi 3krát rychlejší)
- např. set = {"žena", "růže", "píseň"}
- je to samotný datový typ, hodnoty uvnitř jsou stringy
- lze vytvořit i prázdný: prazdny_set = set()
- alternativně set_s_hodnotami = {"hodnota1", "hodnota2", ...}
- nebo taky změnit existující list/tupl na set
- takže je měnitelný
- nemá pořadí
- plus *hodnoty jsou UNIKÁTNÍ (!) a zachovávají se jen unikátní (nejde tak třeba skrz to počítat výskyty nějakých znaků třeba jako u listů)*
- --> je dobré tak pro vyhledávání vzít list a přetypovat na set a pak vyhledávat
- obecně se tak sety hodí na vyhledávání a jejich operace (viz níže)

<h3> Operace nad sety </h3>

- metody setů např.: add, clear, copy, difference, difference_update, discard, intersection, intersection_update, isdisjoint, issubset, issuperset,
pop, remove, symmetric_difference, symmetric_difference_update, union, update
- set1.union(set2) --> výsledkem je sloučení obou setů do 1 setu (set --> unikátních hodnot)
- alternativně jako set1 | set2 (ale moc se to nepoužívá, hlavně na CZ klávesnici je to alt g + W)
- set1.intersection(set2) --> vrátí průnik obou setů
- alternativně (set1 & set2)
- do teď symetrický --> nevadilo prohodit set1 a set2 --> nezáleželo na pořadí; asymetrické --> hraje roli (!)
- set1.difference(set2) --> odečte od setu1 set2 --> vrátí to, co je v setu1 a není v setu2 AKA *vem set1 a odstraň vše, co se nachází v setu2*
- alternativně (set1 - set2)
- když naopak, tak vrátí to, co má unikátní jen set2 (vůči setu1)
- rozdíl set1 - set2 je logicky prázdná množina
- set1.symmetric_difference(set2) --> tady na pořadí nezáleží --> vrátí kombinaci (set1 - set2) + (set2 - set1) AKA *co je unikátní pro každou z množin*
- set.add(prvek_k_přidání) --> přidá 1 definovaný prvek do množiny
- set.discard(prvek_k_odstranění) --> odstraní 1 definovaný prvek z množiny
- set1.isdisjoint(set2) --> vrátí pravdu, když jsou oba sety spojené (?)

<h3> Frozen set </h3>

- nezměnitelný set ("je zmrazený")
- skrze frozenset() fci --> je to fce, takže třeba fs = frozenset((obsahu_setu))
- --> jsou tam dvojité závorky, protože jeden pár patří funkci, druhý k zabalení setu (k řečení, že je to set)
- lze vytvářet ze stringů, ale taky i listů, tuplů a setů (jak sety)
- metody mají fs podobné jak sety, jen se nedají měnit (takže by to hodilo chybu)
- použití: 
1) jako klíč ve slovníku
2) a hlavně indikátor pro ostatní, že se tohle nemá měnit

<h3> Volitelné argumenty </h3>

- viz jupyter
- některé fce mají volitelný počet argumentů - třeba print (dávám tam obsah, separátor, konec řádku, ...)
- a lze tak dále specifikovat/upravovat default nastavení
- v helpu pythunu je to často daný ... (3 tečkama) v dokumentaci

<h2> LEKCE 4 - For cyklus (6.2.2024) </h2>

<h3> Opakování </h3>

- list je měnitelný, hranaté závorky X tuple je NEměnný, kulaté závorky + tuple lze použít jako klíč ve slovníku (list ne)
- ve slovníku, když sáhnu po novém klíči a zadám hodnotu --> vznikne nový pár X když jen sáhnu po novém a nedám hodnotu --> error
- ve slovníku po hodnotě sáhnout místo slovnik["klic"] pomocí slovnik.get("klic") --> první varianta dá chybu (když klíč neexistuje), druhá none, případně specifikovanou hlášku vypíše (např. slovnik.get("klic", "klic neexistuje))
- btw je dobré si při vytvoření nějaké listu, kde se může opakovat hodně hodnot (např. domény mailu), jej převést na set a pak zpátky na list --> zůstanou jen unikátní hodnoty (+ zpátky to chceme na list, protože se setem se blbě pracuje - nedá se indexovat apod.)
- btw f-string: print(f"Číslo je {cislo}") a lze tak přímo ve stringu mít proměnnou (případně pak skrze to i formátovat: např. print(f"{cislo=<10}))

<h3> JSON </h3>

- to, co v Pythonu nazýváme slovník, je jinde (hlavně v JS) JSON - JavaScript Object Notation
- syntax je podobný jak právě u slovníků, případně zanořených slovníků, případně s hodnotami v podobě listů
- má to nějaké specifika JS, třeba True s malým t (které v Python neexistuje)
- každopádně když budeme tahat věci z nějakých služeb (asi jsou tím myšlena APIs), tak to bude ve formátu JSON
- lze to převést do Python pomocí fce get_json("url_služby")
- plus to ideálně přetypujeme předtím (např. int(get_json(...))) a/nebo upravíme/odstraníme nějaké prvky hodnot např. .replace(",","").replace("-","")

<h3> For loop </h3>

- aka smyčka, cyklus
- 2 typy: for, while
- u for např: for cislo in [1, 2, 3, 4]: print(cislo)
-   v hranatých závorkách jsou hodnoty proměnné cislo, které bude nabývat --> vypíše postupně 1 2 3 4
- v podstatě lze odvodit z výpisu: for prvek in sekvenční_datový_typ: ... --> pro každý prvek v datovém typu udělej ...
- to v [] je tedy iterovatelný zdroj hodnot, který postupně ukládá do proměnné jeho hodnoty (AKA sekvenční datový typ)
- může to být přímo samotný list (např. for cisla in (0, 1, 2):...) nebo zastoupené proměnnou, kterou jsem dříve někde uložil (např. for jmena in list_jmen: ...)
- POZOR: není dobré používat v prvku jméno, co už je definované někde jinde --> zůstane tomu pak ta poslední hodnota z iterovatelného datového typu, který použijeme
- NEiterovatelné datové typy: integer, float
- iterovatelné datové typy: list, string, tuple, slovník (vrací klíče), set (ale bez pořadí), range
- zajímavé je to u SLOVNÍKŮ: lze iterovat skrze klíče, hodnoty nebo kombinaci obou (defaultně se prochází dle klíče)
- pokud bychom chtěli jít po hodnotách, je třeba to říct
- ohlášení ve smyčkách --> mění chování smyčky
- break = skončí po dosažení podmínky
- continue = přeskočí hodnotu při naplnění podmínky
- pass = zabraná potenciální vyjímce (vlastně místo chyby tak, aby program pokračoval)
- else u loopu for: lze podobně jako u if použít else, když tam mám vnořenou fci if (třeba hledám nějaký znak --> pokud tam není, spustí se else)
- POZOR: to else je k loopu, ne fci if --> je odsazené stejné jako for --> spustí se po ÚSPĚŠNÉM dokončení (bez breaku!) smyčky
- vnořené for loops: 
-   smyčka jde po jednotlivých iterací --> (vnější) udělá první hodnotu ze zadaných a jde na to, co VŠE má zadáno jako další (ve vnitřní loop)
-   --> když skončí vnitřní loop, jde zpět ke vnějšímu a opakuje ten postup tam-a-zpátky, dokud nedojdou hodnoty (prvně v té vnitřní, pak v té vnější)

<h3> Datový typ range </h3>

- k celočíselným rozsahům (intervalům)
- skrze fci range()
- hlavní smysl je ta iterovatelnost (třeba pro fci loop)
- při printu vypíše jen okrajové, např. range(11) --> range(0, 11)
- 1 argument --> kdy skončit (poslední hodnota tam není); od nuly
- 2 --> kdy začít a kdy skončit (včetně začátku)
- 3 --> začátek, konec, step (po kolika bude skákat)
- lze používat i ve smyčkách: např. for cisla in range(5): print(cisla)
- POZOR: abych to vytisknul, potřebuju před range() mít datový typ - třeba list(range())

<h3> Funkce enumerate </h3>

- zabudovaná fce
- k očíslování iterovatelného objektu, např. list nebo tuple
- podobně jako u range potřebuju datový typ před to: list(enumerate(cisla))
- taky často ve smyčkách podobně jako range --> for pismena in enumerate("Ahoj"): print(pismena) --> výsledkem bude tuple s indexem jako prvním a písmenem jako druhým v pořadí (dle indexů) pro každé písmeno
- pokud chci víc najednou: for index, symbol in enumerate("Ahoj, světe"): print(f"Index: {index}, symbol: {symbol}")

<h3> Funkce ZIP </h3>

- na slepení 2 a víc iterovatelných datových typů
- pokud je jedno kratší než druhý, tak to druhé bude zkráceno ve výsledku
- zase se z toho musí udělat ten nějaký list apod --> např. list(zip(datovy_typ_1, datovy_typ_2))
- výsledkem je tuple

<h2> LEKCE 5 - While cyklus (14.2.2024) </h2>

<h3> opakování z minula </h3>

- for i in zdroj: print(i*2)
- i je ta proměnná, která bude nabývat hodnoty ze zdroje
- za dvojtečkou je to, co se stane pro každou hodnotu ze zdroje
- vždy to, co se má vykonat pro každou hodnotu, musí být odsazené
- integer (třeba 123) se nedá iterovat --> pro 1 hodnotu nemá smysl iterovat
- set, list, tuple nebo dictionary či string (který má víc hodnot/znaků) se dá už iterovat
- ...aka to musí mít délku, aby se tím dalo iterovat --> string "Ahoj" má délku, ale číslo 123 už ne
- ALE v případě použití range (např. range(10)) už lze použít int jako iterovatelný objekt
- range(x) dává vždy vždy prvních x hodnot --> např. range(3) = 0 1 2 (ALE už ne 3!)

<h3> While smyčka </h3>

- vedle for existuje i while
- while provádí ohlášení (to, co je pod ní odsazené), dokud bude zadaná podmínka pravdivá (např. while i < 5: i = i +1>)
- (btw musím si to i definovat před smyčkou, jinak hodí chybu --> žejo, jinak nebude vědět, jak ověřit podmínku)
- btw samozřejmě podmínka může mít víc aspektů (např. i > 5 and i != 3) --> celý výraz musí být true, aby podmínka dál jela
- prostě dokud je TRUE, smyčka jede, jakmile se stane FALSE, smyčka končí
- použití for <-- když chci projít všechny hodnoty
- použití while <-- když chci iterovat za určitých podmínek
- while lze doplnit podmínkou pod tím, taky odsazenou
- někdy je možné napsat dodatečnou podmínku přímo za while, ALE může se tak stát, že skrze kombinaci True a False neprojde vše (skončí), jak bych chtěl
- ohlášení podobně jako u for:
- break: přeskočí zbytek, když je naplněno něco --> typicky se dává do if podvětve
- continue: VRÁCENÍ NA ZAČÁTEK SMYČKY --> typicky taky pod if podvětev (to pod continue ve stejném bloku se nevykoná a smyčka jede dál)
- lze taky doplnit else: else se spustí, když je hlavní podmínka FALSE
-
- BTW POZOR: BREAK PŘERUŠÍ i část pod else

<h3> Nekonečná smyčka </h3>

- kdy je použít? když chci třeba uživatele nutit zadat validní hodnotu nebo nějaký key word --> bude dokola dotazován, dokud to nedá
- 2 typy: neřízené X řízené
- neřízené: to NECHCEME! vzniká při chybě v kódu, když podmínka bude vždy pravdivá (např. while i > 0: i = i + 1 print(i)), ukončuje se pomocí Ctrl + C
- řízené: viz výše --> taková, kde ji lze přerušit zadáním vhodného vstupu (dělá skrze pomocnou proměnnou, která je pořád True, nebo break pod if)

<h3> Přiřazovací operátor </h3>

- aka walrus operátor (emoji mrože :=)
- ke spojení dvou kroků v jedném zápise: uloží hodnotu do proměnné A rovnou ji použije (např. print(jmeno := "Matous"))
- POZOR: walrus musí být v kulaté závorce použit, jinak hodí syntaxError
- POZOR 2: walrus je dostupný od Pythonu 3.8 a výš
- lze použít jako operátor v podmínkách (ale opět musí být v závorce)
- Python to dělá tak, že: 
1) vezme/spočítá hodnotu, kterou bude přiřazovat --> 
2) přiřadí hodnotu --> 
3) použije ji (pokud je to třeba v if clause)
- (v případě if) --> proto se tam dávají ty závorky, jinak by to zpracoval normálně (prvně vyhodnotil/spočítal a pak přiřadil)
- lze taky kombinovat se smyčkou while