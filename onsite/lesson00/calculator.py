import doctest


def vypis_operace(*args):
    """
    Vypiš zadané znaky spojené do jednoho stringu.

    :param args: obsahuje spojitelné hodnoty.
    :type args: tuple[str] nebo str
    :return: funkce nemá žádnou návratovou hodnotu.
    :rtype: None

    :Example:
    >>> vypis_operace("+", "-")
    ---------
    | + | - |
    ---------
    >>> vypis_operace("+", "-", "*")
    -------------
    | + | - | * |
    -------------
    """
    status = f"| {' | '.join(args)} |"
    oddelovac = len(status) * "-"
    print(oddelovac, status, oddelovac, sep="\n")


def vypocitej_prumer(ciselna_rada):
    """
    Vypiš průměrnou hodnotu vypočítanou ze zadaných hodnot.

    :param ciselna_rada: řada čísel oddělených čárkou.
    :type ciselna_rada: str
    :return: funkce vrací desetinnou číselnou hodnotu.
    :rtype: float

    :Example:
    >>> prumer = vypocitej_prumer("1, 2, 3")
    >>> prumer
    2.0
    """
    ciselne_hodnoty = [
        int(char)
        for char in ciselna_rada.split(",")
        if char.strip().isnumeric()
    ]

    return sum(ciselne_hodnoty) / len(ciselne_hodnoty)


def vypocitej_aritm_operace(rce):
    """
    Vrať výsledek pro základní aritmetické operace jak desetinné číslo.

    :param rce: výraz obsahující rovnici.
    :type rce: str
    :return: desetinné číslo jako výsledek rovnice.
    :rtype: float

    :Example:
    >>> vysledek = vypocitej_aritm_operace("((1 + 3) / 2)")
    >>> vysledek
    2.0
    """
    return eval(rce)


def spust_kalkulacku():
    """
    Hlavní funkce, která spouští celou kalkulačku.
    """
    print("spouštím kalkulačku..".upper())
    vstup = ""

    while vstup != "quit":
        vypis_operace("+", "-", "*", "/", "prum", "quit")
        vstup = input("vyber operaci:".upper())

        if vstup in ("+", "-", "*", "/"):
            print("pouze číselné hodnoty doplněné závorkami.".upper())
            print(
                "Výsledek:".upper(),
                vypocitej_aritm_operace(
                    input('zadej rovnici:'.upper())
                    )
            )
        elif vstup == "prum":
            print("pouze číselné hodnoty oddělené čárou.".upper())
            print(
                "Průměrná hodnota:".upper(),
                vypocitej_prumer(
                    input('hodnoty:'.upper())
                )
            )


if __name__ == "__main__":
    # doctest.testdoc()
    spust_kalkulacku()

