class Dlugosc:
    przeliczniki = {
        'm': 1,
        'mm': 0.001,
        'cm': 0.01,
        'dm': 0.1,
        'km': 1000,
        'in': 0.025_4,
        'mi': 1_609.344,
        'ft': 0.304_8
    }
    def __init__(self, wartosc_liczbowa, jednostka):
        self._wartosc_liczbowa = wartosc_liczbowa
        self._jednostka = jednostka
    def __gt__(self, other):
        return self.wartosc_w_m > other.wartosc_w_m
    def __eq__(self, other):
        return self.wartosc_w_m == other.wartosc_w_m
    def __str__(self):
        return f"{self._wartosc_liczbowa:.1f}{self._jednostka}"
    def __repr__(self):
        return f"{type(self).__name__}{repr((self._wartosc_liczbowa, self._jednostka))}"
    def __add__(self, other):
        return type(self)(
            self._wartosc_liczbowa + other.wartosc_w_jednostce(self._jednostka),
            self._jednostka
        )
    def __sub__(self, other):
        # krótsze rozwiązanie:
        # return self + -other
        # tworzy tymczasowy obiekt -other i dodaje go do siebie (potencjalnie mniej wydajne)
        return type(self)(
            self._wartosc_liczbowa - other.wartosc_w_jednostce(self._jednostka),
            self._jednostka
        )
    def __neg__(self):
        return type(self)(
            -self._wartosc_liczbowa,
            self._jednostka
        )
    def __mul__(self, other):
        return type(self)(
            self._wartosc_liczbowa * other,
            self._jednostka
        )
    __rmul__ = __mul__
    # def __rmul__(self, other):
    #    return self * other
    @property
    def wartosc_w_m(self):
        return self._wartosc_liczbowa * self.przeliczniki[self._jednostka]
    def wartosc_w_jednostce(self, jednostka):
        return self.wartosc_w_m / self.przeliczniki[jednostka]
    def przelicz_na(self, jednostka):
        return type(self)(self.wartosc_w_jednostce(jednostka), jednostka)

a = Dlugosc(2, 'km')
b = Dlugosc(3, 'mi')
c = b.przelicz_na('km')
d = a - b
e = -c
f = a * 3
g = 4 * b

dlugosci = [a,b,c,a+c,d,e,f,g]

for dlugosc in dlugosci:
    print(dlugosc)

a = Dlugosc(2, 'km')
b = Dlugosc(200000, 'cm')

print(a == b)
