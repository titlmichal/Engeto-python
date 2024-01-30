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
kontakty = ["telefon" : "+420 739 123 456", "email" : "michal@gmail.com"]
info["kontakty"] = kontakty
print(info["kontakty"])