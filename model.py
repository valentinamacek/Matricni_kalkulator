import numpy as np
import json
import fractions


class Stanje:
    def __init__(self, matrike):
        self.matrike = matrike

    def dodaj_matriko(self, matrika):
        self.matrike.append(matrika)

    def odstrani_matriko(self, matrika):
        self.matrike.remove(matrika)

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
            return {"vsota": "Matriki morata biti iste velikosti"}

    def __mul__(self, other):
        if self.st_stolpcev == other.st_vrstic:
            nova = []
            other_transponiran = other.transponiraj()
            for vrstica in self.matrika:
                novavrst = []
                for stolpec in other_transponiran.matrika:
                    vsota = 0
                    for element_self, element_other in zip(vrstica, stolpec):
                        vsota += element_self * element_other
                    novavrst.append(vsota)
                nova.append(novavrst)
            return Matrika(nova)
        else:
            return {"produkt": "Prva matrika mora imeti toliko stolpcev kot ima druga matrika vrstic"}

    def potenciraj(self, n):
        try:
            float(n)
            if not float(n).is_integer() or float(n) <= 0:
                return {"potenciraj": "Vnesi naravno število"}
            g = float(n)
            c = int(g)
            if self.st_stolpcev == self.st_vrstic:
                k = c - 1
                potencirana = self
                while k != 0:
                    potencirana = potencirana * self
                    k -= 1
                return potencirana
            else:
                return {"potenciraj": "Matrika mora biti kvadratna"}
        except ValueError:
            return {"potenciraj": "Vnesi naravno število"}

    def mnozenje_s_skalar(self, skalar):
        try:
            float(skalar)
        except ValueError:
            try:
                fractions.Fraction(skalar)
                skalar = float(fractions.Fraction(skalar))
            except ValueError:
                return {"skalar": "Vnesi realno število"}
        nova = []
        for vrstica in self.matrika:
            novav = []
            for element in vrstica:
                k = float(skalar) * element
                novav.append(k)
            nova.append(novav)
        return Matrika(nova)

    def det(self):
        # izračuna determinanto matrike na rekurziven način z razvojem po prvi vrstici
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
                for j_stolpec, element in enumerate(self.matrika[0]):
                    brezprve_vrstice = Matrika(self.matrika[1:])
                    brez_j_stolpca = Matrika(
                        np.delete(brezprve_vrstice.matrika, j_stolpec, 1))
                    if j_stolpec % 2 == 0:
                        vsota += element*brez_j_stolpca.det()
                    else:
                        vsota -= element*brez_j_stolpca.det()
                return vsota
        else:
            return {"det": "Matrika mora biti kvadratna"}

    def prirejenka(self):
        if self.st_stolpcev == self.st_vrstic:
            nova = []
            for i_vrstica in range(self.st_vrstic):
                novav = []
                for j_stolpec in range(self.st_stolpcev):
                    k = i_vrstica+j_stolpec
                    brez_i_vrst = Matrika(
                        np.delete(self.matrika, i_vrstica, 0))
                    brez_j_stolpca = Matrika(
                        np.delete(brez_i_vrst.matrika, j_stolpec, 1))
                    if k % 2 == 0:
                        poddet = brez_j_stolpca.det()
                    else:
                        poddet = -brez_j_stolpca.det()
                    novav.append(poddet)
                nova.append(novav)
            return Matrika(nova)
        else:
            return {"prirejenka": "Matrika mora biti kvadratna"}

    def inverz(self):
        if self.st_stolpcev == self.st_vrstic:
            detmat = self.det()
            if detmat != 0:
                prirejenka = self.prirejenka()
                prirejenkaT = prirejenka.transponiraj()
                inverz = prirejenkaT.mnozenje_s_skalar(1/detmat)
                return inverz
            else:
                return {"inverz": "Matrika ni obrnljiva"}
        else:
            return {"inverz": "Matrika ni obrnljiva"}

    def sled(self):
        if self.st_stolpcev == self.st_vrstic:
            sled = 0
            for i in range(self.st_vrstic):
                sled += self.matrika[i][i]
            return sled
        else:
            return {"sled": "Matrika mora biti kvadratna"}

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
        nova = []
        for vrstica in self.matrika:
            novav = []
            for element in vrstica:
                nov = str(fractions.Fraction(element).limit_denominator())
                novav.append(nov)
            nova.append(novav)
        return nova

    @staticmethod
    def spremeni_v_matriko(niz):
        if niz == "":
            return {"matrika": "Še enkrat preberi navodila"}
        else:
            vrstice = niz.split(";")
            seznam = []
            prvavrstica = vrstice[0].split()
            st_stolpcev = len(prvavrstica)
            for vrstica in vrstice:
                seznamv = []
                elementi = vrstica.split()
                if len(elementi) != st_stolpcev:
                    return {"matrika": "To ni matrika"}
                for element in elementi:
                    try:
                        float(element)
                    except ValueError:
                        try:
                            fractions.Fraction(element)
                            element = float(fractions.Fraction(element))
                        except ValueError:
                            return {"matrika": "Še enkrat preberi navodila"}
                    seznamv.append(element)
                seznam.append(seznamv)
            return Matrika(seznam)
