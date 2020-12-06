"""
Napisać funkcję obliczającą całkowity wstępu grupy osób  do kina, wg zasady:
jeden bilet kosztuje 20
przy zakupie co najmniej 10 biletów bilet kosztuje 13
"""

# TODO: zaimplementować funkcję koszt_biletow_grupy(liczba_osob)

def koszt_biletow_grupy(liczba_osob):
    if liczba_osob >= 10:
        cena_biletu = 13
    else:
        cena_biletu = 20
    return liczba_osob * cena_biletu

grupy_testowe = [ 1, 2, 5, 7, 9, 13, 20, 50 ]

for g in grupy_testowe:
    koszt = koszt_biletow_grupy( g )
    print(f"osób: {g}   koszt: {koszt}")
