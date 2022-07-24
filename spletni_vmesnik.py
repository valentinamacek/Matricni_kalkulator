from ssl import OP_ALL
import bottle
from model import Stanje, Matrika, je_matrika_s_stevili
import numpy as np

IME_DATOTEKE = "stanje.json"
try:
    stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Stanje(matrike=[])


@bottle.get("/oblika/<file>")
def staticno_oblikovanje(file):
    return bottle.static_file(file, root="oblika")


@bottle.get("/dodaj-matriko/")
def dodaj_matriko():
    return  bottle.template("dodaj_matriko.tpl", napake={})


@bottle.get("/")
def zacetna_stran():
    return bottle.template(
        "zacetna_stran.tpl",
        matrike=stanje.matrike, operacije=OPERACIJE)

@bottle.post("/dodaj-matriko/")
def dodaj_matriko_post():
    elementi=bottle.request.forms["matrika"]
    if je_matrika_s_stevili(elementi):
        seznam = np.matrix(elementi)
        matrika = Matrika(seznam)
        napake = stanje.preveri_podatke_nove_matrike(matrika)
        if napake:
            return bottle.template("dodaj_matriko.tpl", napake=napake)
        else:
            stanje.dodaj_matriko(matrika)
            bottle.redirect("/")
    else:
        napake={}
        napaka= "Matrični elementi morajo biti števila"
        napake["matrika"]=napaka
        return bottle.template("dodaj_matriko.tpl", napake=napake)



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


@bottle.get("/rezultat_dveh/<id_matrike1:int>/<id_matrike2:int>/<stanje_r:int>")
def prikazi_rezultat_dveh(id_matrike1, id_matrike2, stanje_r):
    napake={}
    matrika1 = stanje.matrike[id_matrike1]
    matrika2 = stanje.matrike[id_matrike2]
    vsota = matrika1 + matrika2
    if isinstance(vsota, Matrika)==False:
       napake["vsota"]="Matriki morata biti iste velikosti"
    produkt = matrika1 * matrika2
    if isinstance(produkt, Matrika)== False:
       napake["produkt"]="Prva matrika mora imeti toliko stolpcev kot ima druga matrika vrstic"
    if stanje_r==1 and isinstance(vsota, Matrika):
            stanje.dodaj_matriko(vsota)
    if stanje_r==2 and isinstance(produkt, Matrika):
            stanje.dodaj_matriko(produkt)
    return bottle.template("rezultat_dveh.tpl", matrika1=matrika1, matrika2=matrika2, vsota=vsota, produkt=produkt,
        id_matrike1=id_matrike1,id_matrike2=id_matrike2, matrike=stanje.matrike, operacije=OPERACIJE, napake=napake)
    
@bottle.post("/dodaj-rezultats/<id_matrike1:int>/<id_matrike2:int>/")
def dodaj_rezultats(id_matrike1, id_matrike2):
    stanje_r=1
    return bottle.redirect(f"/rezultat_dveh/{id_matrike1}/{id_matrike2}/{stanje_r}")
  
@bottle.post("/dodaj-rezultatz/<id_matrike1:int>/<id_matrike2:int>/")
def dodaj_rezultatz(id_matrike1, id_matrike2):
    stanje_r=2
    return bottle.redirect(f"/rezultat_dveh/{id_matrike1}/{id_matrike2}/{stanje_r}")

@bottle.post("/operacija-dveh/")
def operacija_dveh():
    id_matrike1 = bottle.request.forms["matrika1"]
    id_matrike2 = bottle.request.forms["matrika2"]
    stanje_r=0
    return bottle.redirect(f"/rezultat_dveh/{id_matrike1}/{id_matrike2}/{stanje_r}")


OPERACIJE=["transponiraj", "prirejenka", "inverz", "det", "sled", "potenciraj", "mnozenje_s_skalar" ]

@bottle.post("/operacija-ena/")
def operacija_ena():
    id_matrike = bottle.request.forms["matrike"]
    for operacija in OPERACIJE:
        if operacija==bottle.request.forms["operacija"]:
            if operacija=="potenciraj":
                stopnja = bottle.request.forms["stopnja_potence"]
                return bottle.redirect(f"/potenciraj_rezultat/{id_matrike}/{stopnja}")
            elif operacija=="mnozenje_s_skalar":
                skalar = bottle.request.forms["zeljen_skalar"]
                return bottle.redirect(f"/mnozenje_s_skalar_rezultat/{id_matrike}/{skalar}")
            else:
                return bottle.redirect(f"/{operacija}_rezultat/{id_matrike}/")
            
bottle.run(debug=True, reloader=True)