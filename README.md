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

***ÚKOL DO PŘÍSTĚ NA VYZKOUŠENÍ V JUPYTERU***

<h2> LEKCE 2 - Podmínky a metody (24.1.2024) </h2>

<h3> Boolean </h3>

- příp. bool
- o pravdivosti (TRUE X FALSE)
-   true je basically 1, false 0 --> boolean je basically special case integer
- funkce bool jako rozhodčí --> print(bool(....)), i když to bool tam být asi nemusí, záleží prý

<h3> Srovnávání </h3>

- často u těch booleanů
- > < >= <= == (rovná se) != (nerovná se) is (je totožné) is not (různá objektová identita)

<h3> Boolean procesy </h3>

- všechno je objekt v Pythonu
- --> vše má své označení (lze zjistit pomocí fce id)
-   identické hodnoty = stejné číslo, tedy adresu objektu v paměti PC
- mají své operátory: and, or not
-   and: např. True and True (výsledek True) ... jakmile by viděl False --> výsledek False
-   plus *zkrácené vyhodnocení* - vidí False na další se už ani nepodívá
-   or: stačí jeden True a je to celé True
-   not: dává se jednomu objektu a obrací hodnotu True --> False X False --> True
- *pořadí vyhodnocování*: not --> and --> or
- ověřování členství
-   zda je něco v něčem - např. ("M" in "Michal"), nebo není --> ("M" not in "Brno") ... oboje True
-   btw stejná skupina funkce jako slicing, indexing, striding, ...