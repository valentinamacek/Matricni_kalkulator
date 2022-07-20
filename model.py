import numpy as np
import json
import fractions

def je_matrika_s_stevili(niz):
    assert isinstance(niz, str)
    try: 
        np.matrix(niz)
        return True
    except ValueError:
        return False
    

class Stanje:
    def __init__(self, matrike):
        self.matrike = matrike

    def dodaj_matriko(self, matrika):
        self.matrike.append(matrika)
        

    def preveri_podatke_nove_matrike(self, nova_matrika):
        for matrika in self.matrike:
            if matrika == nova_matrika:
                return {"matrika": "Taka matrika je že v tvojem seznamu"}

    def v_slovar(self):
        return {
            "matrike": [matrika.v_slovar() for matrika in self.matrike],
        }

    @staticmethod
    def iz_slovarja(slovar):
        stanje = Stanje(
            [
                Matrika.iz_slovarja(slovarmatrika)
                for slovarmatrika in slovar["matrike"]
            ]
        )
        return stanje

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat, indent=4, ensure_ascii=False)

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke) as dat:
            slovar = json.load(dat)
            return Stanje.iz_slovarja(slovar)


class Matrika:
    def __init__(self, matrika):
        self.matrika = np.array(matrika, dtype='float64')
        self.st_vrstic = len(self.matrika)
        self.st_stolpcev = len(self.matrika[0])

    def transponiraj(self):
        return Matrika(self.matrika.transpose())
    
    def __eq__(self, other):
        return np.array_equal(self.matrika, other.matrika)

    def __add__(self, other):
        if self.st_stolpcev == other.st_stolpcev and self.st_vrstic == other.st_vrstic:
            return Matrika(self.matrika + other.matrika)
        else:
            print("Matriki morata biti iste velikosti")

    def __mul__(self, other):
        if self.st_stolpcev == other.st_vrstic:
            nova = []
            othert = other.transponiraj()
            for vrstica in self.matrika:
                novavrst = []
                for stolpec in othert.matrika:
                    vsota = 0
                    for element, oelement in zip(vrstica, stolpec):
                        vsota += element*oelement
                    novavrst.append(vsota)
                nova.append(novavrst)
            return Matrika(nova)
        else:
            print("Prva matrika mora imeti toliko stolpcev kot ima druga matrika vrstic")

    def potenciraj(self, n):
        if n >= 0 and float(n).is_integer():
            g=float(n)
            c=int(g)
            if self.st_stolpcev == self.st_vrstic:
                k = c-1
                potencirana = self
                while k != 0:
                    potencirana = potencirana * self
                    k -= 1
                return potencirana
            else:
                print("Vnesi kvadratno matriko")
        else:
            print("Vnesi nenegativno celo stevilo")

    def mnozenje_s_skalar(self, skalar):
        nova = []
        for vrstica in self.matrika:
            novav = []
            for element in vrstica:
                k = skalar * element
                novav.append(k)
            nova.append(novav)
        return Matrika(nova)

    def det(self):
        if self.st_stolpcev == self.st_vrstic:
            n = self.st_stolpcev
            if n == 1:
                return self.matrika[0][0]
            elif n == 2:
                vsota = self.matrika[0][0]*self.matrika[1][1] - \
                    self.matrika[0][1]*self.matrika[1][0]
                return vsota
            else:
                vsota = 0
                for i, element in enumerate(self.matrika[0]):
                    brezprve = Matrika(self.matrika[1:])
                    brezprvet = brezprve.transponiraj()
                    brezistolpca = Matrika(np.delete(brezprvet.matrika, i, 0))
                    if i % 2 == 0:
                        vsota += element*brezistolpca.det()
                    else:
                        vsota -= element*brezistolpca.det()
                return vsota
        else:
            print("Matrika mora biti kvadratna")

    def prirejenka(self):
        if self.st_stolpcev == self.st_vrstic:
            nova = []
            for i in range(self.st_vrstic):
                novav = []
                for j in range(self.st_stolpcev):
                    k = i+j
                    brez_i_vrst = Matrika(np.delete(self.matrika, i, 0))
                    brez_i_vrstt = brez_i_vrst.transponiraj()
                    brez_j_stolpca = Matrika(
                        np.delete(brez_i_vrstt.matrika, j, 0))
                    if k % 2 == 0:
                        poddet = brez_j_stolpca.det()
                    else:
                        poddet = -brez_j_stolpca.det()
                    novav.append(poddet)
                nova.append(novav)
            return Matrika(nova)
        else:
            print("Matrika mora biti kvadratna")

    def inverz(self):
        if self.st_stolpcev == self.st_vrstic:
            detmat = self.det()
            if detmat != 0:
                prirejenka = self.prirejenka()
                prirejenkaT = prirejenka.transponiraj()
                inverz = prirejenkaT.mnozenje_s_skalar(1/detmat)
                return inverz
            else:
                print("Matrika ni obrnljiva")
        else:
            print("Matrika ni obrnljiva")

    def sled(self):
        sled = 0
        for i in range(self.st_vrstic):
            sled += self.matrika[i][i]
        return sled

    def v_slovar(self):
        seznam = self.matrika.tolist()
        return {
            "matrika": seznam,
            "st_vrstic": self.st_vrstic,
            "st_stolpcev": self.st_stolpcev,
        }
    @staticmethod
    def iz_slovarja(slovar):
        return Matrika(slovar["matrika"])
    
    def spremeni_obliko_matrike(self):
        nova=[]
        for vrstica in self.matrika:
            novav=[]
            for element in vrstica:
                nov= str(fractions.Fraction(element).limit_denominator())
                novav.append(nov)
            nova.append(novav)
        return nova