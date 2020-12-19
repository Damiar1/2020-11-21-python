def siema(x):
    print("Siema!")

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

print(Osoba)
o1 = Osoba("Jan", "Kowalski", 82, 1.76)
print(o1)

o2 = Osoba("Monika", "Xyz", 50, 1.63)
o3 = Osoba("Basia", "Abc", 53, 1.57)
osoby = [o1, o2, o3]
print(osoby)

o4 = Osoba("Wojciech", "Lalala", 78, 1.77)
print(o4.witaj)
o4.witaj(600)
o4.przedstaw_sie()

o4.pokaz_bmi()

if o4.bmi() < 20:
    print("Uuuuuu, niedożywiony.")
else:
    print("Wszystko w porządku")

o5 = Osoba("Grzegorz", "Fff", 73, 1.77)
