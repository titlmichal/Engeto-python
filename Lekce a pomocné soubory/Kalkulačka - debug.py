# Kalkulačka - debug

import os

def spocitat_zakladni_op() -> None:
    """"""
    zapis = "("
    while True:
        tlacitko = input("TLACITKO: ")
        if tlacitko.isnumeric() or tlacitko in ("-", "+"):
            zapis += str(tlacitko)
        elif tlacitko in ("/", "*"):
            zapis += f"){tlacitko}("
        elif tlacitko == "=":
            zapis += ")" if zapis[:-1] != ")" else ""
            print("VYSLEDEK: ", eval(zapis))
            break


def spocitat_prumer() -> None:
    """ """
    rada_cisel = list()
    while (hodnota := input("Dalsi cislo: ")) != "quit":
        if hodnota.isnumeric():
            rada_cisel.append(float(hodnota))
    os.system("clear")
    print("PRUMER: ", sum(rada_cisel) / len(rada_cisel))
    print()


def umocneni_exp() -> None:
    """"""
    hodnota = float(input("Hodnota: "))
    mocnina = float(input("Mocnina: "))
    os.system("clear")
    print(
        "VYSLEDEK: ",
        hodnota ** mocnina,
    )


def kalkulacka():
    """"""
    procesy = ("zakladni_op", "prum", "pow", "quit")
    while True:
        vyber = input("VYBER OPERACI: ")
        if vyber not in procesy:
            print("Neexistujici operace")
            continue
        if vyber == "qui":
            break
        elif vyber == "pow":
            umocneni_exp()
        elif vyber == "prum":
            spocitat_prumer()
        else:
            # elif vyber == "zakladni_op":
            spocitat_zakladni_op()


if __name__ == "__main__":
    kalkulacka()