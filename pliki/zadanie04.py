# Napisać program, który zapyta użytkownika o kod waluty
# a następnie pobierze z NBP kurs z ostatnich kilkunastu dni
# i wygeneruje wykres w formacie SVG.

import json
import requests

URL = "http://api.nbp.pl/api/exchangerates/rates/A/%s/last/%d/?format=JSON"

def rysuj_wykres(dane, nazwapliku):
    SZER = 800
    WYS = 600
    MARGIN = 20
    ODSTEP = 10
    f = open(nazwapliku, "w")
    f.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
    f.write(f'<svg width="{SZER}" height="{WYS}" xmlns="http://www.w3.org/2000/svg">')
    maxwartosc = 0
    for etykieta, wartosc in dane:
        if wartosc > maxwartosc:
            maxwartosc = wartosc
    x = MARGIN
    for etykieta, wartosc in dane:
        wysokosc = wartosc/maxwartosc * (WYS-2*MARGIN)
        szer = (SZER-2*MARGIN-(len(dane)-1)*ODSTEP )/len(dane)
        y = ODSTEP+(maxwartosc-wartosc)/maxwartosc*(WYS-2*MARGIN)
        f.write(f'<rect x="{x}" y="{y}" width="{szer}" height="{wysokosc}" fill="#f00" stroke="#000" />')
        x+=szer+ODSTEP
    f.write('</svg>')

#waluta = input("Podaj kod waluty: ")
waluta = "EUR"
ile = 13

url = URL % ( waluta, ile )

kursy = [ (k['effectiveDate'], k['mid']) for k in json.loads(requests.get(url).text)['rates'] ]

rysuj_wykres( kursy, "zadanie04.svg")