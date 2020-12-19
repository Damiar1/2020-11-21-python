def siema(x):
    print("Siema!")

class Osoba:
    _imie = "nienazwany"
    _nazwisko = "nieznane"
    _waga = 0
    _wzrost = 0
    def __init__(self):
        print("Hurra! Jestem nową osobą!!!!!!!!")
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

print(Osoba)
#o1 = Osoba("Jan", "Kowalski", 82, 1.76)
o1 = Osoba()
print(o1)

o2 = Osoba()
o3 = Osoba()
osoby = [o1, o2, o3]
print(osoby)

o4 = Osoba()
print(o4.witaj)
o4.witaj(600)

o4.ustaw_imie("Mateusz")
o4.ustaw_nazwisko("AAAA")

o4.przedstaw_sie()

o4._waga = 60
o4._wzrost = 1.8

o4.pokaz_bmi()

if o4.bmi() < 20:
    print("Uuuuuu, niedożywiony.")
else:
    print("Wszystko w porządku")
