Poznámky ke kurzu

*ÚVOD - 17.1.2024* 
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

*LEKCE 1 - ÚVOD DO PROGRAMOVÁNÍ*

**1.1 Úvod do programování**
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

***Syntax***
- patří sem ty fce, podmínky, smyčky, ...
- Python zarovnává do bloků (viz PEP 8)

***Číselné hodnoty/datové typy***
= kufříky, které mají nějaký tvar, který se liší dle toho, co do něj vkládáme
- python umožňuje do tohoto kufříku dávat čísla i řetězce (líp se píše, hůř identifikuje chyba) --> použití fce type()
- str() jako řetězec; int() jako celá čísla; float() jako desetinná
- klasické operátory; navíc to dělení na desetinná čísla / a celá // a modulo % (tj. zbytek po dělení)
- problém s float (viz platforma, že 0.1+0.2 se nerovná přesně 0.3), řešitelné knihovnou decimal