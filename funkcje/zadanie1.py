"""
Napisać kod funkcji pokaz_ucznia, która wyświetli informacje o uczniu w takiej formie:

Imie:       Jan
Nazwisko:   Kowalski
Oceny:      3,5,6,3,2...
Średnia:    4.59

funkcja ma być wywoływana w taki sposób:

pokaz_ucznia( uczen1 )
"""

uczen1 = {"imie": "Katarzyna", "nazwisko": "H.", "oceny": "3 4 4 5 4 3 3 5 5 5"}
uczen2 = { "imie" : "Kosma", "nazwisko" : "I.", "oceny" : "3 4 4 3 3 3 4 4 4 4" }

def pokaz_ucznia( uczen ):
    oceny = [int(o) for o in uczen['oceny'].split()]
    srednia = sum(oceny)/len(oceny)
    print(f"{'Imie:':11} {uczen['imie']}")
    print(f"{'Nazwisko:':11} {uczen['nazwisko']}")
    print(f"{'Oceny:':11} {','.join([str(o) for o in oceny])}")
    print(f"{'Średnia':11} {srednia}")

# wywołanie funkcji:
pokaz_ucznia(uczen1)
#pokaz_ucznia(uczen2)

