import bottle
from model import Stanje, spremeni_obliko


IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(matrike=[])

@bottle.get("/")
def zacetna_stran():
     return bottle.template(
        "zacetna_stran.tpl",
      matrike = stanje.matrike, spremeni_obliko=spremeni_obliko)



bottle.run(debug=True, reloader=True)