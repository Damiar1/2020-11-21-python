class Dlugosc:
    def __init__(self, wartosc_liczbowa, jednostka):
        self._wartosc_liczbowa = wartosc_liczbowa
        self._jednostka = jednostka
    # TODO: funkcja przeliczająca różne jednostki na metry

x1 = Dlugosc(1.8, 'm')
x2 = Dlugosc(175, 'cm')
x3 = Dlugosc(40, 'in')

print(x1)

# 1.8m > 175cm -- powinno wyjść True
if x1 > x2:
    print("ok")