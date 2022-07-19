from model import Stanje, Matrika
import numpy as np
import fractions
np.set_printoptions(formatter={'all': lambda x: str(fractions.Fraction(x).limit_denominator())})
IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(matrike=[])


def preberi_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vnesti morate število.")


def izberi_moznost(moznosti):
    """Uporabniku našteje možnosti ter vrne izbrano."""
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f"{i}) {opis}")
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznost, _opis = moznosti[i - 1]
            return moznost
        else:
            print(f"Vnesti morate število med 1 in {len(moznosti)}.")


def transponiraj_matriko(seznam):
    transponirana = seznam.transponiraj()
    stanje.dodaj_matriko(transponirana)
    print(prikaz_Matrike(transponirana))


def determinanta_od_matrike(seznam):
    det = seznam.det()
    rezultat = f"{det}"
    print(rezultat)


def prirejenka_od_matrike(seznam):
    prirejenka = seznam.prirejenka()
    stanje.dodaj_matriko(prirejenka)
    print(prikaz_Matrike(prirejenka))


def inverz_matrike(seznam):
    inverz = seznam.inverz()
    stanje.dodaj_matriko(inverz)
    print(prikaz_Matrike(inverz))


def sled_matrike(seznam):
    sled = seznam.sled()
    rezultat = f"{sled}"
    print(rezultat)


def potenciraj_matriko(seznam, n):
    potencirana = seznam.potenciraj(n)
    stanje.dodaj_matriko(potencirana)
    print(prikaz_Matrike(potencirana))


def mnozenje_s_skalarjem(seznam, k):
    produkt = seznam.mnozenje_s_skalar(k)
    stanje.dodaj_matriko(produkt)
    print(prikaz_Matrike(produkt))


def sestej(matrika1, matrika2):
    assert isinstance(matrika1, Matrika) and isinstance(matrika2, Matrika)
    vsota = matrika1 + matrika2
    stanje.dodaj_matriko(vsota)
    print(prikaz_Matrike(vsota))


def zmnozi(matrika1, matrika2):
    assert isinstance(matrika1, Matrika) and isinstance(matrika2, Matrika)
    produkt = matrika1*matrika2
    stanje.dodaj_matriko(produkt)
    print(prikaz_Matrike(produkt))


def prikaz_Matrike(seznam):
    niz = f"{seznam.matrika}\n stevilo vrstic:{seznam.st_vrstic}\n stevilo stolpcev:{seznam.st_stolpcev}"
    return niz


def izpisi_trenutno_stanje():
    for matrika in stanje.matrike:
        print(prikaz_Matrike(matrika))
    if not stanje.matrike:
        print(
            "Trenutno nimate še nobene matrike"
        )


def moznosti_posz(seznam):

    izbrana_operacija = izberi_moznost(
        [
            (transponiraj_matriko, "transponiraj matriko"),
            (determinanta_od_matrike, "izračunaj determinanto"),
            (prirejenka_od_matrike, "izračunaj prirejenko matrike"),
            (inverz_matrike, "izračunaj inverz matrike"),
            (sled_matrike, "izracunaj sled matrike"),
            (potenciraj_matriko, "potenciraj matriko "),
            (mnozenje_s_skalarjem, "pomnozi matriko s skalarjem"),
        ]
    )
    if izbrana_operacija!=potenciraj_matriko and izbrana_operacija != mnozenje_s_skalarjem:
        izbrana_operacija(seznam)
    else:
        if izbrana_operacija==potenciraj_matriko:
            print("Vnesi željeno stopnjo")
            n = input()
            if n.isdigit():
                izbrana_operacija(seznam , int(n))
            else:
                print("Vnesi celo stevilo")
        else:
            print("Vnesi željen skalar")
            k= input()
            try:
                float(k)
                izbrana_operacija(seznam, float(k))
            except ValueError:
                print("Vnesi stevilo")
                   

def moznosti_dveh(seznam1, seznam2):
    izbrana_operacija = izberi_moznost(
        [
            (sestej, "seštej matriki"),
            (zmnozi, "zmnoži matriki"),
        ]
    )
    izbrana_operacija(seznam1, seznam2)


def je_matrika_s_stevili(niz):
    assert isinstance(niz, str)
    for znak in niz:
        if znak.isdigit() == False:
            if znak != ';' and znak != ',' and znak != ' ':
                return False
    return True


def izberi_matriko(stanje):
    print("Izberi matriko:")
    return izberi_moznost(
        [
            (matrika, prikaz_Matrike(matrika))
            for matrika in stanje.matrike
        ]
    )


def dodaj_matriko():
    print("Vnesi matriko")
    vnos = input()
    if je_matrika_s_stevili(vnos) == True:
        seznam = np.matrix(vnos)
        matrika = Matrika(seznam)
        stanje.dodaj_matriko(matrika)
    else:
        print("Vnesi stevila")


def zacetni_pozdrav():
    print("Pozdravljeni v matričnem kalkulatorju")


def zakljuci_izvajanje():
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    print("Nasvidenje!")
    exit()


def ponudi_moznosti():
    if not stanje.matrike:
        dodaj_matriko()
    else:
        izbrano_dejanje = izberi_moznost(
            [
                (dodaj_matriko, "dodaj matriko"),
                (operacije_z_matriko, "izberi 1 matriko"),
                (operacije_dveh_matrik, "izberi 2 matriki"),
                (zakljuci_izvajanje, "izhod"),
            ]
        )
        izbrano_dejanje()


def operacije_z_matriko():
    matrika = izberi_matriko(stanje)
    moznosti_posz(matrika)


def operacije_dveh_matrik():
    matrika1 = izberi_matriko(stanje)
    matrika2 = izberi_matriko(stanje)
    moznosti_dveh(matrika1, matrika2)


def tekstovni_vmesnik():
    zacetni_pozdrav()
    while True:
        izpisi_trenutno_stanje()
        ponudi_moznosti()


tekstovni_vmesnik()
