"""
Napisać funkcję obliczającą całkowity wstępu grupy osób  do kina, wg zasady:
jeden bilet kosztuje 20
przy zakupie co najmniej 10 biletów bilet kosztuje 13
"""

# TODO: zaimplementować funkcję koszt_biletow_grupy(liczba_osob)

def koszt_biletow_grupy(liczba_osob):
    cena_zwykla = 20
    cena_grupowa = 13
    min_grupa = 10
    return liczba_osob * cena_grupowa if liczba_osob >= min_grupa else cena_zwykla

grupy_testowe = [ 1, 2, 5, 7, 9, 13, 20, 50 ]

for g in grupy_testowe:
    koszt = koszt_biletow_grupy( g )
    print(f"osób: {g}   koszt: {koszt}")
