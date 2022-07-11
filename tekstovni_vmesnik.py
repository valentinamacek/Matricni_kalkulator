from model import Matrika
import json
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
    zacetna=Matrika(seznam)
    print(zacetna.matrika)
    transponirana= zacetna.transponiraj()
    print(transponirana.matrika)
    return transponirana.matrika

# def vnesi_matriko():
#     seznam= input()
#     matrika=Matrika(seznam)
#     print(matrika.matrika)
#     return matrika
def je_matrika(seznam):
    if isinstance(seznam, list):
        for element in seznam:
            if isinstance(element, list)==False:
                return False
        return True
    else:
        return False

def ponudi_moznosti(seznam):
    izbrana_operacija= izberi_moznost(
        [
            (transponiraj_matriko, "transponiraj matriko")
            # (determinanta_od_matrike, "izračunaj determinanto")
            # (prirejenka_od_matrike, "izračunaj prirejenko matrike")
            # (inverz_matrike, "izračunaj inverz matrike")
        ]
    )
    izbrana_operacija(seznam)

def tekstovni_vmesnik():
    vnos =input()
    if vnos[0]=='[' and vnos.endswith(']'):
        seznam = json.loads(vnos)
        if je_matrika(seznam)==True:
            ponudi_moznosti(seznam)
        else:
            print("To ni matrika")
    else:
        print("To ni matrika")

