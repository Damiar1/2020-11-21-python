"""
Napisać funkcję obliczającą całkowity wstępu grupy osób  do kina, wg zasady:
jeden bilet kosztuje 20
przy zakupie co najmniej 10 biletów bilet kosztuje 13
"""

# TODO: zaimplementować funkcję koszt_biletow_grupy(liczba_osob)

def koszt_biletow_grupy(liczba_osob, cennik):
    return liczba_osob * ( cennik["cena_grupowa"] if liczba_osob >= cennik["min_grupa"] else cennik["cena_zwykla"] )

grupy_testowe = [ 1, 2, 5, 7, 9, 13, 20, 50 ]

c1 = {
    "cena_zwykla" : 20,
    "cena_grupowa" : 13,
    "min_grupa" : 10
}

c2 = {
    "cena_zwykla": 19,
    "cena_grupowa": 14,
    "min_grupa": 12
}

for g in grupy_testowe:
    koszt = koszt_biletow_grupy(g, c1)
    koszt2 = koszt_biletow_grupy(g, c2)
    print(f"osób: {g}   koszt: {koszt}   koszt2: {koszt2}")
