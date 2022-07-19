import bottle
from model import Stanje, Matrika


IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(matrike=[])


@bottle.get("/oblika/<file>")
def staticno_oblikovanje(file):
    return bottle.static_file(file, root="oblika")


@bottle.get("/")
def zacetna_stran():
    return bottle.template(
        "zacetna_stran.tpl",
        matrike=stanje.matrike)


@bottle.get("/transponiraj_rezultat/<id_matrike:int>/")
def transponiraj_rezultat(id_matrike):
    matrika = stanje.matrike[id_matrike]
    transponirana = matrika.transponiraj()
    return bottle.template("transponiraj_rezultat.tpl", matrika=matrika, transponirana=transponirana)


@bottle.get("/prirejenka_rezultat/<id_matrike:int>/")
def prirejenka_rezultat(id_matrike):
    matrika = stanje.matrike[id_matrike]
    prirejena = matrika.prirejenka()
    return bottle.template("prirejenka_rezultat.tpl", matrika=matrika, prirejena=prirejena)


@bottle.get("/inverz_rezultat/<id_matrike:int>/")
def inverz_rezultat(id_matrike):
    matrika = stanje.matrike[id_matrike]
    inverz = matrika.inverz()
    return bottle.template("inverz_rezultat.tpl", matrika=matrika, inverz=inverz)


@bottle.get("/det_rezultat/<id_matrike:int>/")
def det_rezultat(id_matrike):
    matrika = stanje.matrike[id_matrike]
    determinanta = matrika.det()
    return bottle.template("det_rezultat.tpl", matrika=matrika, determinanta=determinanta)


@bottle.get("/sled_rezultat/<id_matrike:int>/")
def sled_rezultat(id_matrike):
    matrika = stanje.matrike[id_matrike]
    sled = matrika.sled()
    return bottle.template("sled_rezultat.tpl", matrika=matrika, sled=sled)


@bottle.get("/potenciraj_rezultat/<id_matrike:int>/<stopnja>")
def potenciraj_rezultat(id_matrike, stopnja):
    matrika = stanje.matrike[id_matrike]
    rezultat = matrika.potenciraj(float(stopnja))
    return bottle.template("potenciraj_rezultat.tpl", matrika=matrika, rezultat=rezultat, stopnja=stopnja, Matrika=Matrika)


@bottle.get("/mnozenje_s_skalar_rezultat/<id_matrike:int>/<skalar>")
def mnozenje_s_skalar_rezultat(id_matrike, skalar):
    matrika = stanje.matrike[id_matrike]
    rezultat = matrika.mnozenje_s_skalar(float(skalar))
    return bottle.template("mnozenje_s_skalar_rezultat.tpl", matrika=matrika, rezultat=rezultat, skalar=skalar)


@bottle.get("/zmnozi_rezultat/<id_matrike1:int>/<id_matrike2:int>")
def zmnozi_rezultat(id_matrike1, id_matrike2):
    matrika1 = stanje.matrike[id_matrike1]
    matrika2 = stanje.matrike[id_matrike2]
    produkt = matrika1 * matrika2
    return bottle.template("zmnozi_rezultat.tpl", matrika1=matrika1, matrika2=matrika2, produkt=produkt)


@bottle.get("/sestej_rezultat/<id_matrike1:int>/<id_matrike2:int>")
def sestej_rezultat(id_matrike1, id_matrike2):
    matrika1 = stanje.matrike[id_matrike1]
    matrika2 = stanje.matrike[id_matrike2]
    vsota = matrika1 + matrika2
    return bottle.template("sestej_rezultat.tpl", matrika1=matrika1, matrika2=matrika2, vsota=vsota)


@bottle.post("/transponiraj/")
def transponiraj():
    id_matrike = bottle.request.forms.getunicode("matrike")
    return bottle.redirect(f"/transponiraj_rezultat/{id_matrike}/")


@bottle.post("/prirejenka/")
def prirejenka():
    id_matrike = bottle.request.forms.getunicode("matrike")
    return bottle.redirect(f"/prirejenka_rezultat/{id_matrike}/")


@bottle.post("/inverz/")
def inverz():
    id_matrike = bottle.request.forms.getunicode("matrike")
    return bottle.redirect(f"/inverz_rezultat/{id_matrike}/")


@bottle.post("/det/")
def det():
    id_matrike = bottle.request.forms.getunicode("matrike")
    return bottle.redirect(f"/det_rezultat/{id_matrike}/")


@bottle.post("/sled/")
def sled():
    id_matrike = bottle.request.forms.getunicode("matrike")
    return bottle.redirect(f"/sled_rezultat/{id_matrike}/")


@bottle.post("/potenciraj/")
def potenciraj():
    id_matrike = bottle.request.forms.getunicode("matrike")
    stopnja = bottle.request.forms["stopnja_potence"]
    return bottle.redirect(f"/potenciraj_rezultat/{id_matrike}/{stopnja}")


@bottle.post("/mnozenje_s_skalar/")
def mnozenje_s_skalar():
    id_matrike = bottle.request.forms.getunicode("matrike")
    skalar = bottle.request.forms["zeljen_skalar"]
    return bottle.redirect(f"/mnozenje_s_skalar_rezultat/{id_matrike}/{skalar}")


@bottle.post("/zmnozi/")
def zmnozi():
    id_matrike1 = bottle.request.forms.getunicode("matrika1")
    id_matrike2 = bottle.request.forms.getunicode("matrika2")
    return bottle.redirect(f"/zmnozi_rezultat/{id_matrike1}/{id_matrike2}")


@bottle.post("/sestej/")
def sestej():
    id_matrike1 = bottle.request.forms.getunicode("matrika1")
    id_matrike2 = bottle.request.forms.getunicode("matrika2")
    return bottle.redirect(f"/sestej_rezultat/{id_matrike1}/{id_matrike2}")


bottle.run(debug=True, reloader=True)
