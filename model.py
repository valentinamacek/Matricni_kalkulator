import numpy as np
from fractions import Fraction
class Matrika:
    def __init__(self, matrika):
        self.matrika = np.array(matrika)
        self.st_vrstic=len(matrika)
        self.st_stolpcev=len(matrika[0])
    def transponiraj(self):
        return Matrika(self.matrika.transpose())
    def __add__(self, other):
        if self.st_stolpcev == other.st_stolpcev and self.st_vrstic == other.st_vrstic:
            return Matrika(self.matrika + other.matrika)
        else:
            print("Matriki morata biti iste velikosti")
    def __mul__(self, other):
        if self.st_stolpcev == other.st_vrstic:
            nova=[]
            othert=other.transponiraj()
            for vrstica in self.matrika:
                novavrst=[]
                for stolpec in othert.matrika:
                    vsota=0
                    for element, oelement in zip(vrstica, stolpec): 
                        vsota+=element*oelement
                    novavrst.append(vsota)
                nova.append(novavrst)
            return Matrika(nova)
        else:
            print("Prva matrika mora imeti toliko stolpcev kot ima druga matrika vrstic")
    def mnozenje_s_skalar(self, skalar):
        nova =[]
        for vrstica in self.matrika:
            novav=[]
            for element in vrstica:
                k= skalar * element
                g=float(k)
                if g.is_integer():
                  novav.append(k)
                else:
                  ulomek = Fraction(g).limit_denominator()
                  novav.append(ulomek)
            nova.append(novav)
        return Matrika(nova)
    def det(self):
        if self.st_stolpcev == self.st_vrstic:
            n = self.st_stolpcev
            if n==1:
                return self.matrika[0][0]
            elif n == 2:
               vsota = self.matrika[0][0]*self.matrika[1][1]-self.matrika[0][1]*self.matrika[1][0]
               return vsota
            else:
                vsota=0
                for i,element in enumerate(self.matrika[0]):
                    brezprve=Matrika(self.matrika[1:])
                    brezprvet=brezprve.transponiraj()
                    brezistolpca=Matrika(np.delete(brezprvet.matrika, i, 0))
                    if i%2==0:
                        vsota+=element*brezistolpca.det()
                    else:
                        vsota-=element*brezistolpca.det()
                return vsota
        else:
            print("Matrika mora biti kvadratna")
    def prirejenka(self):
        if self.st_stolpcev == self.st_vrstic:
            nova=[]
            for i in range(self.st_vrstic):
                novav=[]
                for j in range(self.st_stolpcev):
                    k=i+j
                    brez_i_vrst=Matrika(np.delete(self.matrika, i, 0))
                    brez_i_vrstt=brez_i_vrst.transponiraj()
                    brez_j_stolpca=Matrika(np.delete(brez_i_vrstt.matrika, j, 0))
                    if  k%2==0:
                        poddet=brez_j_stolpca.det()
                    else:
                        poddet=-brez_j_stolpca.det()
                    novav.append(poddet)
                nova.append(novav)
            return Matrika(nova)
        else:
            print("Matrika mora biti kvadratna")
    def inverz(self):
        if self.st_stolpcev == self.st_vrstic:
            detmat=self.det()
            if detmat!=0:
                prirejenka=self.prirejenka()
                prirejenkaT=prirejenka.transponiraj()
                inverz=prirejenkaT.mnozenje_s_skalar(1/detmat)
                return inverz
            else:
                print("Matrika ni obrnljiva")
        else:
            print("Matrika ni obrnljiva")
# print inverz:
# import fractions
# np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})
#  print(k.matrika)
    def sled(self):
        sled=0
        for i in range(self.st_vrstic):
            sled+=self.matrika[i][i]
        return sled 
                        
   