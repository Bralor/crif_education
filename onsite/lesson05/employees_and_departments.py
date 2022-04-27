import time
from random import random
from random import randint
from random import choice
from pprint import pprint

from unidecode import unidecode

zamestnanci_raw = """
Helena Vybíralová
Wendy Štrumlová
Marie Vybíralová
Stanislav Bechyňka
Zdeňka Urbánková
Lukáš Riečan
Veronika Koudelová
Františka Vorlová
Ilie Seleš
Martin Železný
Petra Niklesová
Bohumil Skok
Jakub Šmíd
Jarmila Procházková
Dagmar Hlavatá
Jiří Nguyen Thanh
Marie Franková
Dana Ulrichová
Jana Hranická
Hana Budošová
Ivan Široký
Květoslava Jiráčková
Pavel Przywara
Josef Umlauf
Tomáš Granzer
Miroslav Kuba
Miloslava Adámková
Marie Karlíková
Jaroslav Hronský
Vlasta Karlíková
Andrea Žatková
Zuzana Lokočová
Ondřej Ptáček
Zdeněk Najman
Tereza Šebešová
Antonie Skokánková
Jan Lion
Václav Vecko
František Vajgl
Adéla Kavková
Amália Vacková
Anna Pažická
Ivo Pustějovský
Antonín Pavela
Jitka Adamová
Libuše Hamroziová
Drahomíra Balzerová
Marek Suchánek
Petr Vavrinec
Jonáš Stuchlý
Jaromír Pecen
Markéta Kyliánková
Marina Pečenková
Ivana Perdochová
Michaela Drápalová
Michael Mentlík
Rudolf Špičák
Žaneta Holá
Blanka Lišková
Eva Svatoňová
Rostislav Hoang
Martina Kalivodová
Milan Hruška
Zdenka Marková
Lenka Schambergerová
Růžena Martinů
Věra Řezanková
Marie Pečenková
Miloš Váchal
Jaroslava Hrubá
Petr Pecen
Pavla Konvicová
Lucie Marešová
Květuše Zdráhalová
Vlastimila Svatošová
Zora Michalčíková
Daniel Švejnoha
Klára Brunclíková
Vladimír Bauer
Michal Slaný
Jiřina Novosadová
Karel Sršeň
Stanislava Lakosilová
Filip Černý
Alena Kubiková
Sára Kotrlová
Alois Rejlek
Božena Novotná
Maryana Nováková
Kateřina Máslová
Ladislav Dvořák
Radek Varga
Petr Dvořák
Ludmila Jaklová
Renáta Foubíková
Nikola Lehká
Dominika Riegerová
Patrik Polák
Soňa Štrbová
David Matoušek
Liubov Hollíková
Monika Poláková
Marie Jaklová
Aleš Svoboda
Roman Kolínský
Karolína Košiková
"""
oddeleni_raw  = "sales, marketing, hr, development, it"

# Jména & příjmení
vsechna_jmena = list()
vsechna_prijmeni = list()

for cele_jmeno in zamestnanci_raw.splitlines():
    if cele_jmeno:
        vsechna_jmena.append(cele_jmeno.split()[0])
        vsechna_prijmeni.append(cele_jmeno.split()[1])

# Telefonní čísla
tel_cisla = list()

for jmeno in set(vsechna_jmena):
    cislo = ""

    while len(cislo) != 9:
        cislo += str(randint(0, 9))
        formatovane_cislo = f"+ 420 {cislo[:3]} {cislo[3:6]} {cislo[6:]}"
    tel_cisla.append(formatovane_cislo)

# Emailové adresy
emailove_adresy = list()

for jmeno, prijmeni in zip(set(vsechna_jmena), set(vsechna_prijmeni)):
    if jmeno and prijmeni:
        emailove_adresy.append(unidecode(
            f"{jmeno[0].lower()}.{prijmeni.lower()}@firma.cz"
            )
        )

# Datum nástupu
nastupni_datum = list()

for jmeno in set(vsechna_jmena):
    start_str = "01/01/1990"
    konec_str = "01/01/2020"
    format_ = "%d/%m/%Y"

    formatovany_start = time.mktime(time.strptime(start_str, format_))
    formatovany_konec = time.mktime(time.strptime(konec_str, format_))
    prodleva = random()

    vysledek = formatovany_start + prodleva*(formatovany_konec - formatovany_start)
    nastupni_datum.append(time.strftime(format_, time.localtime(vysledek)))

# Jméno oddělení
jmena_oddeleni = list()

for jmeno in oddeleni_raw.split():
    if jmeno:
        jmena_oddeleni.append(jmeno)

# ID vedoucího
id_vedouci = list()

while len(id_vedouci) != 5:
    identifikator = randint(1, 100)

    if identifikator in id_vedouci:
        continue
    id_vedouci.append(identifikator)

# Budget oddělení
budget = list()

while len(budget) != 5:
    castka = choice(range(500_000, 5_000_001, 100_000))
    budget.append(castka)

# Slovník se zaměstnanci
zamestnanci = {
    "zamestnanec_id": tuple(range(1, len(set(vsechna_jmena)) + 1)),
    "jmeno": tuple(vsechna_jmena),
    "prijmeni": tuple(vsechna_prijmeni),
    "telefon": tuple(tel_cisla),
    "email": tuple(emailove_adresy),
    "vytvoreno": tuple(nastupni_datum)
}

# Slovník s odděleními
oddeleni = {
    "oddeleni_id": tuple(range(1, len(jmena_oddeleni) + 1)),
    "oddeleni_jmeno": tuple(jmena_oddeleni),
    "vedouci_id": tuple(id_vedouci),
    "budget": tuple(budget)
}

pprint(zamestnanci)
