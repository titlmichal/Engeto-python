# vstupni promenne
mesta = [
    "Praha", "Viden", "Olomouc",
    "Svitavy", "Zlin", "Ostrava"
]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180"""

# pozdravit uzivatele
# vypsat nabidku
print(
    "VITEJTE U NASI APLIKACE DESTINATIO!",
    cara,
    nabidka,
    cara,
    sep="\n"
)

# ziskat vstupy od uzivatele
na_misto = input("Destinace:")
print(cara)

index_mesta = mesta.index(na_misto)
cena = ceny[index_mesta]

# vypis informace uzivateli
print(f"Cena listku je {cena}")