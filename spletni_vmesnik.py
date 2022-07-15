import bottle
from model import Stanje, Matrika
import numpy as np
import fractions
np.set_printoptions(formatter={'all': lambda x: str(
    fractions.Fraction(x).limit_denominator())})

IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(matrike=[])

@bottle.get("/")
def zacetna_stran():
     return bottle.template(
        "zacetna_stran.tpl",
      matrike = stanje.matrike)



bottle.run(debug=True, reloader=True)