import random
# dokumentacja modułu random: https://docs.python.org/3/library/random.html

class Osoba:
    def __init__(self, imie, nazwisko, waga, wzrost):
        self._imie = imie
        self._nazwisko = nazwisko
        self._waga = waga
        self._wzrost = wzrost
    def witaj(self, a):
        print(f"Witam {a}! {self}")
    def przedstaw_sie(self):
        print(f"Nazywam się {self._imie} {self._nazwisko}")
    def pokaz_bmi(self):
        print(f"Moje BMI: {self.bmi():.1f}")
    def bmi(self):
        return self._waga/self._wzrost**2
    def ustaw_imie(self, imie):
        self._imie = imie
    def ustaw_nazwisko(self, nazwisko):
        self._nazwisko = nazwisko
    @staticmethod
    def ocen_zdrowie(bmi):
        # https://pl.wikipedia.org/wiki/Wska%C5%BAnik_masy_cia%C5%82a#Zakresy_warto%C5%9Bci_BMI
        if bmi < 16.0:
            return "wygłodzenie"
        elif bmi < 17.0:
            return "wychudzenie"
        elif bmi < 18.5:
            return "niedowaga"
        elif bmi < 25.0:
            return "ok"
        elif bmi < 30.0:
            return "nadwaga"
        else:
            return "otyłość"

# TODO: napisać funkcję generującą losowe osoby
# (niekoniecznie o nazwie xxx...)
osoby = [xxx() for i in range(10)]

for o in osoby:
    o.przedstaw_sie()
    o.pokaz_bmi()
    print(f"stan_zdrowia: {Osoba.ocen_zdrowie(o.bmi())}")