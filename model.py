import numpy as np
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
     
   