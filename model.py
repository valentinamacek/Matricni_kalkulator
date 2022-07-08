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
        