from data.udaje import byty
from vzor.prevodnik import vzory


def rozdel_data(data: str) -> tuple:
    """
    Projdi puvodni data a rozdel zaznamy po radcich.
    """
    return tuple(
        [
            byt
            for byt in data.splitlines()
            if byt
        ]
    )


def parsuj_zaznam(zaznam: str):
    """
    Rozdel jednotny string podle carek na 4 dilci hodnoty.
    """
    return zaznam.split(",", maxsplit=3)


def vytvor_nova_data(puvodni_data: tuple) -> tuple:
    """
    Vrat tuple s prevedenymi hodnotami z puvodni struktury.
    """
    nova_data = list()

    for puvodni_byt in puvodni_data:
        typ_bytu, plocha, obec, ulice = parsuj_zaznam(puvodni_byt)
        nova_data.append(
            ",".join(
                (
                    vzory.get(typ_bytu, "neexistujici_typ"),
                    plocha,
                    obec,
                    ulice
                )
            )
        )

    return tuple(nova_data)


