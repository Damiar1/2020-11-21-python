"""
Napisz program zliczajacy liczbe unikalnych liczb wprowadzonych
przez uzytkownika. Sprawdz jak duzo z tych liczb jest liczbami
parzystymi w zakresie 0-100.
"""

liczby = set()

while True:
    x = input("Podaj liczbe (lub KONIEC):")
    if x.lower() == 'koniec':
        break
    xx = int(x)
    if 0 <= xx <= 100 and xx % 2 == 0:
        liczby.add(xx)

print(f"Zbiór: {liczby}")
print(f"Liczba elementów: {len(liczby)}")

