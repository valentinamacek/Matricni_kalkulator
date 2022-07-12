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
    niz=print(transponirana.matrika)
    return niz

def determinanta_od_matrike(seznam):
    det=seznam.det()
    rezultat= f"{det}"
    print(rezultat)
    return rezultat
   


def ponudi_moznosti(seznam):
    izbrana_operacija= izberi_moznost(
        [
            (transponiraj_matriko, "transponiraj matriko"),
            (determinanta_od_matrike, "izračunaj determinanto"),
            # (prirejenka_od_matrike, "izračunaj prirejenko matrike"),
            # (inverz_matrike, "izračunaj inverz matrike")
        ]
    )
    izbrana_operacija(seznam)

def je_matrika_s_stevili(niz):
    assert isinstance(niz, str)
    for znak in niz:
        if znak.isdigit()==False:
            if znak!=';' and znak!=',' and znak!=' ':
                return False
    return True

def dodaj_matriko():
        print("Vnesi matriko")
        vnos =input()
        if je_matrika_s_stevili(vnos)==True:
            seznam=np.matrix(vnos)
            matrika=Matrika(seznam)
            stanje.dodaj_matriko(matrika)
            ponudi_moznosti(matrika)
        else:
            print("Vnesi stevila")



