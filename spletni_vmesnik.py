from ssl import OP_ALL
import bottle
from model import Stanje, Matrika
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

@bottle.post("/izberi_stevilo/")
def izbira_st_matrik():
    stevilo=bottle.request.forms["izbira"]
    if stevilo=="ena":
        bottle.redirect("/operacije-ena/")
    else:
        bottle.redirect("/operacije-dve/")

@bottle.get("/operacije-ena/")
def operacije_ena_prikaz():
    return bottle.template("operacije_ena.tpl", matrike=stanje.matrike, operacije=OPERACIJE)

@bottle.get("/operacije-dve/")
def operacije_dve_prikaz():
    return bottle.template("operacije_dve.tpl", matrike=stanje.matrike, operacije=OPERACIJE)

@bottle.post("/dodaj-matriko/")
def dodaj_matriko_post():
    elementi=bottle.request.forms["matrika"]
    pretvorba=Matrika.spremeni_v_matriko(elementi)
    if isinstance(pretvorba, Matrika):
        napake = stanje.preveri_podatke_nove_matrike(pretvorba)
        if napake:
            return bottle.template("dodaj_matriko.tpl", napake=napake)
        else:
            stanje.dodaj_matriko(pretvorba)
            bottle.redirect("/")
    else:
        return bottle.template("dodaj_matriko.tpl", napake=pretvorba)



@bottle.get("/potenciraj_rezultat/<id_matrike:int>/<stopnja>/")
def potenciraj_rezultat(id_matrike, stopnja):
    matrika = stanje.matrike[id_matrike]
    rezultat = matrika.potenciraj(float(stopnja))
    return bottle.template("potenciraj_rezultat.tpl", matrika=matrika, rezultat=rezultat, stopnja=stopnja, Matrika=Matrika)





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
    elif stanje_r==2 and isinstance(produkt, Matrika):
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


OPERACIJE=["transponiraj", "prirejenka", "inverz", "det", "sled"]

@bottle.get("/rezultat_ene/<id_matrike:int>/<stanje_r:int>/<skalar>/<stopnja>/")
def prikazi_rezultat_ene(id_matrike, stanje_r, skalar, stopnja):
    napake={}
    matrika = stanje.matrike[id_matrike]
    transponirana = matrika.transponiraj()
    prirejenka = matrika.prirejenka()
    if isinstance(prirejenka, Matrika)==False:
        napake.update(prirejenka)
    inverz = matrika.inverz()
    if isinstance(inverz, Matrika)==False:
        napake.update(inverz)
    determinanta = matrika.det()
    if isinstance(determinanta, float)==False:
        napake.update(determinanta)
    sled = matrika.sled()
    if isinstance(sled, float)==False:
        napake.update(sled)
    if stanje_r==1 :
        stanje.dodaj_matriko(transponirana)
    elif stanje_r==2 and isinstance(prirejenka, Matrika):
        stanje.dodaj_matriko(prirejenka)
    elif stanje_r==3 and isinstance(inverz, Matrika):
        stanje.dodaj_matriko(inverz)
    if skalar=='s' and stopnja=='p':
        return bottle.template("rezultat_ene.tpl", matrika=matrika, transponirana=transponirana, prirejenka=prirejenka, 
        inverz=inverz, determinanta=determinanta, sled=sled, skalar=skalar, stopnja=stopnja,
        id_matrike_izbrana=id_matrike, matrike=stanje.matrike, operacije=OPERACIJE, napake=napake) 
    elif skalar!='s' and stopnja=='p':
        rezultat_mnozenjas = matrika.mnozenje_s_skalar(skalar)
        if isinstance(rezultat_mnozenjas, Matrika)==False:
            napake.update(rezultat_mnozenjas)
        return bottle.template("rezultat_ene.tpl", matrika=matrika, transponirana=transponirana, prirejenka=prirejenka, 
        inverz=inverz, determinanta=determinanta, sled=sled, skalar=skalar, stopnja=stopnja, rezultat_mnozenjas=rezultat_mnozenjas,
        id_matrike_izbrana=id_matrike, matrike=stanje.matrike, operacije=OPERACIJE, napake=napake) 
    elif skalar=='s' and stopnja!='p':
        rezultat_potenciranja = matrika.potenciraj(float(stopnja))
        if isinstance(rezultat_potenciranja, Matrika)==False:
            napake.update(rezultat_potenciranja)
        return bottle.template("rezultat_ene.tpl", matrika=matrika, transponirana=transponirana, prirejenka=prirejenka, 
        inverz=inverz, determinanta=determinanta, sled=sled, skalar=skalar, stopnja=stopnja, rezultat_potenciranja=rezultat_potenciranja,
        id_matrike_izbrana=id_matrike, matrike=stanje.matrike, operacije=OPERACIJE, napake=napake)
    else:
        rezultat_mnozenjas = matrika.mnozenje_s_skalar(skalar)
        rezultat_potenciranja = matrika.potenciraj(float(stopnja))
        return bottle.template("rezultat_ene.tpl", matrika=matrika, transponirana=transponirana, prirejenka=prirejenka, 
        inverz=inverz, determinanta=determinanta, sled=sled, skalar=skalar, stopnja=stopnja, rezultat_potenciranja=rezultat_potenciranja,
        rezultat_mnozenjas=rezultat_mnozenjas,
        id_matrike_izbrana=id_matrike, matrike=stanje.matrike, operacije=OPERACIJE, napake=napake)


@bottle.post("/operacija-ena/")
def operacija_ena():
    id_matrike = bottle.request.forms["matrike"]
    stanje_r=0
    skalar='s'
    stopnja='p'
    return bottle.redirect(f"/rezultat_ene/{id_matrike}/{stanje_r}/{skalar}/{stopnja}/")


@bottle.post("/mnozenje_s_skalar_rezultat/<id_matrike:int>/")
def mnozenje_s_skalar(id_matrike):
    skalar = bottle.request.forms["zeljen_skalar"]
    stanje_r=0
    stopnja='p'
    return bottle.redirect(f"/rezultat_ene/{id_matrike}/{stanje_r}/{skalar}/{stopnja}/")


@bottle.post("/potenciraj_rezultat/<id_matrike:int>/")
def potenciraj(id_matrike):
    stopnja = bottle.request.forms["stopnja_potence"]
    skalar='s'
    stanje_r=0
    return bottle.redirect(f"/rezultat_ene/{id_matrike}/{stanje_r}/{skalar}/{stopnja}/")    
            
bottle.run(debug=True, reloader=True)