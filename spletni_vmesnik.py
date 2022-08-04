from ssl import OP_ALL
import bottle
from model import Stanje, Matrika
import numpy as np

SIFRIRNI_KLJUC = "To je skrivnost"
OPERACIJE=["transponiraj", "prirejenka", "inverz", "det", "sled"]

def ime_uporabnikove_datoteke(uporabnisko_ime):
    return f"stanja_uporabnikov/{uporabnisko_ime}.json"

def stanje_trenutnega_uporabnika():
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    if uporabnisko_ime == None:
        bottle.redirect("/prijava/")
    else:
        uporabnisko_ime = uporabnisko_ime
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    try:
        stanje = Stanje.preberi_iz_datoteke(ime_datoteke)
    except FileNotFoundError:
        stanje = Stanje.preberi_iz_datoteke("stanje.json")
        stanje.shrani_v_datoteko(ime_datoteke)
    return stanje

def shrani_stanje_trenutnega_uporabnika(stanje):
    uporabnisko_ime = bottle.request.get_cookie("uporabnisko_ime", secret=SIFRIRNI_KLJUC)
    ime_datoteke = ime_uporabnikove_datoteke(uporabnisko_ime)
    stanje.shrani_v_datoteko(ime_datoteke)

@bottle.get("/prijava/")
def prijava_get():
    return bottle.template(
        "prijava.tpl"
    )

@bottle.post("/prijava/")
def prijava_post():
    uporabnisko_ime = bottle.request.forms.getunicode("uporabnisko_ime")
    geslo = bottle.request.forms.getunicode("geslo")
    bottle.response.set_cookie("uporabnisko_ime", uporabnisko_ime, path="/", secret=SIFRIRNI_KLJUC)
    bottle.redirect("/")
    

@bottle.post("/odjava/")
def odjava_post():
    bottle.response.delete_cookie("uporabnisko_ime", path="/")
    bottle.redirect("/")


@bottle.get("/oblika/<file>")
def staticno_oblikovanje(file):
    return bottle.static_file(file, root="oblika")


@bottle.get("/dodaj-matriko/")
def dodaj_matriko():
    return  bottle.template("dodaj_matriko.tpl", napake={})

@bottle.get("/odstrani-matriko/")
def odstrani_matriko():
    stanje=stanje_trenutnega_uporabnika()
    return  bottle.template("odstrani_matriko.tpl", matrike=stanje.matrike, napake={})

@bottle.get("/")
def zacetna_stran():
    stanje=stanje_trenutnega_uporabnika()
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
    stanje=stanje_trenutnega_uporabnika()
    return bottle.template("operacije_ena.tpl", matrike=stanje.matrike, operacije=OPERACIJE)

@bottle.get("/operacije-dve/")
def operacije_dve_prikaz():
    stanje=stanje_trenutnega_uporabnika()
    return bottle.template("operacije_dve.tpl", matrike=stanje.matrike, operacije=OPERACIJE)

@bottle.post("/dodaj-matriko/")
def dodaj_matriko_post():
    stanje=stanje_trenutnega_uporabnika()
    elementi=bottle.request.forms["matrika"]
    pretvorba=Matrika.spremeni_v_matriko(elementi)
    if isinstance(pretvorba, Matrika):
        napake = stanje.preveri_podatke_nove_matrike(pretvorba)
        if napake:
            return bottle.template("dodaj_matriko.tpl", napake=napake)
        else:
            stanje.dodaj_matriko(pretvorba)
            shrani_stanje_trenutnega_uporabnika(stanje)
            bottle.redirect("/")
    else:
        return bottle.template("dodaj_matriko.tpl", napake=pretvorba)

@bottle.post("/odstrani-matriko/")
def odstrani_matriko_post():
    stanje=stanje_trenutnega_uporabnika()
    izbrane=[]
    for id_matrike in range(len(stanje.matrike)):
        if bottle.request.forms.get(f"{id_matrike}")!= None:
           izbrane.append(id_matrike)
    if izbrane==[]:
        napake = {"izbor" : "Izberi vsaj eno matriko , ki jo želiš izbrisati, ali pritisni prekliči"}
        return  bottle.template("odstrani_matriko.tpl", matrike=stanje.matrike, napake=napake)
    else:
        print(izbrane)
        izbrane_matrike=[]
        for id_izbrane_matrike in izbrane:
            izbrana_matrika=stanje.matrike[id_izbrane_matrike]
            izbrane_matrike.append(izbrana_matrika)
        for izbrana_matrika in izbrane_matrike:
            stanje.odstrani_matriko(izbrana_matrika)
        shrani_stanje_trenutnega_uporabnika(stanje)
        bottle.redirect("/")
        
@bottle.post("/operacija-dve/<stanje_r:int>/<id_matrike1>/<id_matrike2>/")
def operacija_dve(stanje_r, id_matrike1, id_matrike2):
    stanje=stanje_trenutnega_uporabnika()
    if id_matrike1=='n' and id_matrike2=='n':
        id_matrike1 = int(bottle.request.forms["matrika1"])
        id_matrike2 =int(bottle.request.forms["matrika2"])
    napake={}
    matrika1 = stanje.matrike[int(id_matrike1)]
    matrika2 = stanje.matrike[int(id_matrike2)]
    vsota = matrika1 + matrika2
    if isinstance(vsota, Matrika)==False:
       napake.update(vsota)
    produkt = matrika1 * matrika2
    if isinstance(produkt, Matrika)== False:
       napake.update(produkt)
    if stanje_r==1 and isinstance(vsota, Matrika):
        napaka = stanje.preveri_podatke_nove_matrike(vsota)
        if not napaka:
            stanje.dodaj_matriko(vsota)
            shrani_stanje_trenutnega_uporabnika(stanje)
    elif stanje_r==2 and isinstance(produkt, Matrika):
        napaka = stanje.preveri_podatke_nove_matrike(produkt)
        if not napaka:
            stanje.dodaj_matriko(produkt)
            shrani_stanje_trenutnega_uporabnika(stanje)
    return bottle.template("rezultat_dveh.tpl", matrika1=matrika1, matrika2=matrika2, vsota=vsota, produkt=produkt,
        id_matrike1=id_matrike1,id_matrike2=id_matrike2, matrike=stanje.matrike, operacije=OPERACIJE, napake=napake)
    

@bottle.post("/operacija-ena/<stanje_r:int>/<id_matrike>/<stopnja>/<skalar>/")
def operacija_ena(stanje_r, id_matrike, stopnja, skalar):
    stanje=stanje_trenutnega_uporabnika()
    if id_matrike=='n':
       id_matrike = int(bottle.request.forms["matrike"])
    napake={}
    matrika = stanje.matrike[int(id_matrike)]
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
    if stanje_r==1:
        napaka = stanje.preveri_podatke_nove_matrike(transponirana)
        if not napaka:
            stanje.dodaj_matriko(transponirana)
            shrani_stanje_trenutnega_uporabnika(stanje)
    else:
         stanje=stanje_trenutnega_uporabnika()
    if stanje_r==2 and isinstance(prirejenka, Matrika):
        napaka = stanje.preveri_podatke_nove_matrike(prirejenka)
        if not napaka:
            stanje.dodaj_matriko(prirejenka)
            shrani_stanje_trenutnega_uporabnika(stanje)
    elif stanje_r==3 and isinstance(inverz, Matrika):
        napaka = stanje.preveri_podatke_nove_matrike(inverz)
        if not napaka:
            stanje.dodaj_matriko(inverz)
            shrani_stanje_trenutnega_uporabnika(stanje)
    if  stopnja!='p':
        if stopnja=='n':
            stopnja = bottle.request.forms.getunicode("stopnja_potence")
        rezultat_potenciranja = matrika.potenciraj(stopnja)
        if isinstance(rezultat_potenciranja, Matrika)==False:
            napake.update(rezultat_potenciranja)
        else:
             if stanje_r==4:
                napaka = stanje.preveri_podatke_nove_matrike(rezultat_potenciranja)
                if not napaka:
                    stanje.dodaj_matriko(rezultat_potenciranja)
                    shrani_stanje_trenutnega_uporabnika(stanje)
    else:
          rezultat_potenciranja=''
    if skalar!='s':
        if skalar=='n':
           skalar = bottle.request.forms.getunicode("zeljen_skalar")
        rezultat_mnozenjas = matrika.mnozenje_s_skalar(skalar)
        if isinstance(rezultat_mnozenjas, Matrika)==False:
            napake.update(rezultat_mnozenjas)
        else:
           if stanje_r==5:
               napaka = stanje.preveri_podatke_nove_matrike(rezultat_mnozenjas)
               if not napaka:
                stanje.dodaj_matriko(rezultat_mnozenjas)
                shrani_stanje_trenutnega_uporabnika(stanje)
    else:
        rezultat_mnozenjas=""
    return bottle.template("rezultat_ene.tpl", matrika_izbrana=matrika, transponirana=transponirana, prirejenka=prirejenka, 
    inverz=inverz, determinanta=determinanta, sled=sled, skalar=skalar, stopnja=stopnja, rezultat_potenciranja=rezultat_potenciranja,
    rezultat_mnozenjas=rezultat_mnozenjas,
    id_matrike_izbrana=id_matrike, matrike=stanje.matrike, operacije=OPERACIJE, napake=napake)

@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!" 
            
bottle.run(debug=True, reloader=True)