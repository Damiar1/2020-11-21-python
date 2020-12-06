"""
Napisać funkcję obliczającą całkowity wstępu grupy osób  do kina, wg zasady:
jeden bilet kosztuje 20
przy zakupie co najmniej 10 biletów bilet kosztuje 13
"""

# TODO: zaimplementować funkcję koszt_biletow_grupy(liczba_osob)

def koszt_biletow_grupy(liczba_osob):
    return liczba_osob * 13 if liczba_osob >= 10 else 20

grupy_testowe = [ 1, 2, 5, 7, 9, 13, 20, 50 ]

for g in grupy_testowe:
    koszt = koszt_biletow_grupy( g )
    print(f"osób: {g}   koszt: {koszt}")
