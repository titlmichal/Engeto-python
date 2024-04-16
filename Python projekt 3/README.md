<h1> Election scraper </h1>

Milý uživateli,
vítej v mé variaci na třetí projekt Engeto Akademie (Data/Python), jehož výsledkem je, při nejhorším zdánlivě fukční Python skript umožňující stahovat a ukládat data o volbách v roce 2017 ve zvoleném období do zvoleného souboru. Jelikož se jedná o projekt apolitický, přestože politicky zaměřen, v tomto souboru najdeš především praktické informace, jak skript použít, nikoliv hodnocení výsledků samotných.

<h3> Co je potřeba </h3>

Základním předpokladem pro úspěšné spuštění skriptu je počítač s běžným operačním systémem a rozumným připojením k internetu. Co se týče více "softwarových požadavků, ty konkrétně najdeš v souboru requirements.txt. Základem je programovací jazyk Python, který některé OS už mají built-in. Dále pak knihovny, které nejsou zabudované přímo v jazyce (např. sys, csv), v tomto případě zejména beautifulsoup4 a requests. Před samotnou instalací/spuštěním je vhodné použít virtuální prostředí. To lze vytvořit pomocí konzole/příkazového řádku a skrze něj se dostat do složky, kde je uložen tento skript (election scraper.py). Následně příkazem 'python -m vevn vami_zvoleny_nazev_prostredi' jej vytvoříte a dalším příkazem 'vami_zvoleny_nazev_prostredi\Scripts\activate' aktivujete. Zde pomocí přikazu 'pip list' ověříte aktuální verze/dostupnost knihoven a případně je nainstalujete pomocí příkazů 'pip install nazev_knihovny==verze_knihovny'. Pokud znovu zadáte příkaz na ověření verzí aktivních knihoven ve vašem virtuálním prostředí a seznam odpovídá tomu ve výše zmíněném textovém souboru, můžete se přesunout k používání.

<h3> Použití skriptu </h3>

Stále mějte aktivované virtuální prostředí a zadejte 'python "election scraper.py" "odkaz_na_oblast_ke_stažení" "nazev_cilového_souboru_s_koncovkou.csv"'. Seznam oblastí, na které lze použít tento skript najdete zde (https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ). Je důležité zmínit, že jako argument za název skriptu.py je nutné použít odkaz v celém formátu (tj. od 'https...'), na který se dostanete po kliknutí na 'X' ve sloupci 'Výběr obce' (v žádném jiném!). Jiné odkazy zapříčiní nefunkčnost/jiné fungování skriptu. Druhým argumentem je pak název souboru s koncovkou .csv, který vytvoří a kam skript uloží získaná data. Zároveň je potřeba dodržet pořadí argumentů, v opačném případě dojde k předčasnému ukončení programu. Pokud zadáte příkaz do přikazového řádku dle tohoto textu, skript by vám měl oznámit, že zpracovává data. To je znamení dobrého fungování. Tento krok chvíli trvá v závislosti na vícero faktorech, ale neměl by zabrat více než několik desítek vteřin až velmi nízkých jednotek minut. Po úspěšném zapsání dat do souboru vám tuto zprávu skript sdělí.

<h3> Příklady vhodných příkazů </h3>

python "election scraper.py" "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204" "Zlín.csv"
... stáhne výsledky z oblasti Zlína a zapíše je do souboru Zlín.csv

python "election scraper.py" "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103" "Prostějov.csv"
... stáhne výsledky z oblasti Prostějova a zapíše je do souboru Prostějov.csv

<h3> Příklady nevhodných příkazů </h3>

python "election scraper.py" "Zlín.csv" "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204"
...pořadí argumentů název cílového souboru a zdrojového odkazu je opačné

python "election scraper.py" "https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=1" "Praha.csv"
...odkaz (pod kódem oblasti, zde CZ0100) odkazuje na výsledky celé oblasti, na jejíž zpracování není skript připraven

python "election scraper.py" "https://volby.cz/pls/ps2017nss/ps31?xjazyk=CZ&xkraj=1&xnumnuts=1100" "Praha.csv"
...odkaz (pod 'X' ve sloupci 'Výběr PM') odkazuje na výsledky dle přebíracího místa, na jejichž zpracování není skript připraven