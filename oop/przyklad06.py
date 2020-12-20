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
    def __str__(self):
        return f"{self._wartosc_liczbowa:.1f}{self._jednostka}"
    def __repr__(self):
        return f"{type(self).__name__}{repr((self._wartosc_liczbowa, self._jednostka))}"
    @property
    def wartosc_w_m(self):
        return self._wartosc_liczbowa * self.przeliczniki[self._jednostka]

a = Dlugosc(2, 'km')
b = Dlugosc(3, 'mi')
# TODO:
c = b.przelicz_na('m')

print([a,b,c])
