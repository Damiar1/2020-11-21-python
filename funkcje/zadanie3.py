"""
Napisać funkcję obliczającą całkowity wstępu grupy osób  do kina, wg zasady:
jeden bilet kosztuje 20
przy zakupie co najmniej 10 biletów bilet kosztuje 13
Przy co najmniej 150 osobach koszt jest stały i wynosi 1600.00 za całość.
"""

def koszt_biletow_grupy(liczba_osob, cennik):
    return ( cennik['cena_sali'] if liczba_osob >= cennik['min_sala']
        else liczba_osob * ( cennik["cena_grupowa"] if liczba_osob >= cennik["min_grupa"]
        else cennik["cena_zwykla"] ) )

grupy_testowe = [ 1, 2, 5, 7, 9, 13, 20, 50, 140, 160 ]

c1 = {
    "cena_zwykla" : 20,
    "cena_grupowa" : 13,
    "min_grupa" : 10,
    "cena_sali" : 1600,
    "min_sala" : 150
}

c2 = {
    "cena_zwykla": 19,
    "cena_grupowa": 14,
    "min_grupa": 12,
    "cena_sali": 1600,
    "min_sala": 150

}

for g in grupy_testowe:
    koszt = koszt_biletow_grupy(g, c1)
    koszt2 = koszt_biletow_grupy(g, c2)
    print(f"osób: {g}   koszt: {koszt}   koszt2: {koszt2}")
