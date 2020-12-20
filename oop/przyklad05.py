class Dlugosc:
    def __init__(self, wartosc_liczbowa, jednostka):
        self._wartosc_liczbowa = wartosc_liczbowa
        self._jednostka = jednostka
    def wartosc_w_m(self):
        if self._jednostka == 'm':
            return self._wartosc_liczbowa
        if self._jednostka == 'cm':
            return self._wartosc_liczbowa / 100
        if self._jednostka == 'in':
            return self._wartosc_liczbowa * 0.025_4
        if self._jednostka == 'km':
            return self._wartosc_liczbowa * 1000
        if self._jednostka == 'mi':
            return self._wartosc_liczbowa * 1_609.344

x1 = Dlugosc(1.8, 'm')
x2 = Dlugosc(175, 'cm')
x3 = Dlugosc(40, 'in')

dlugosci = [ x1, x2, x3 ]

for x in dlugosci:
    print(x.wartosc_w_m())
