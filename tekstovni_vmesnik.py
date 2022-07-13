from model import Stanje,Matrika
import numpy as np

IME_DATOTEKE = "1.stanje.json"
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
    transponirana= seznam.transponiraj()
    stanje.dodaj_matriko(transponirana)
    print(transponirana.matrika)

def determinanta_od_matrike(seznam):
    det=seznam.det()
    rezultat= f"{det}"
    print(rezultat)

def sestej(matrika1, matrika2):
    assert isinstance(matrika1, Matrika) and isinstance(matrika2, Matrika)
    vsota= matrika1 + matrika2
    stanje.dodaj_matriko(vsota)
    print(vsota.matrika)

def zmnozi(matrika1, matrika2):
    assert isinstance(matrika1, Matrika) and isinstance(matrika2, Matrika)
    produkt=matrika1*matrika2
    stanje.dodaj_matriko(produkt)
    print(produkt.matrika)

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
    izbrana_operacija= izberi_moznost(
        [
            (transponiraj_matriko, "transponiraj matriko"),
            (determinanta_od_matrike, "izračunaj determinanto"),
            # (prirejenka_od_matrike, "izračunaj prirejenko matrike"),
            # (inverz_matrike, "izračunaj inverz matrike")
        ]
    )
    izbrana_operacija(seznam)

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
        if znak.isdigit()==False:
            if znak!=';' and znak!=',' and znak!=' ':
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
        vnos =input()
        if je_matrika_s_stevili(vnos)==True:
            seznam=np.matrix(vnos)
            matrika=Matrika(seznam)
            stanje.dodaj_matriko(matrika)
            moznosti_posz(matrika)
        else:
            print("Vnesi stevila")

def zacetni_pozdrav():
    print("Pozdravljeni v matričnem kalkulatorju")

def ponudi_moznosti():
    if not stanje.matrike:
        dodaj_matriko()
    elif len(stanje.matrike)==2:
        matrika1=stanje.matrike[0]
        matrika2=stanje.matrike[1]
        moznosti_dveh(matrika1, matrika2)
    elif len(stanje.matrike)==1:
        matrika=stanje.matrike[0]
        moznosti_posz(matrika)
    else:
        matrika1 = izberi_matriko(stanje)
        matrika2 = izberi_matriko(stanje)
        moznosti_dveh(matrika1, matrika2)

def tekstovni_vmesnik():
    zacetni_pozdrav()
    while True:
        izpisi_trenutno_stanje()
        ponudi_moznosti()

tekstovni_vmesnik()