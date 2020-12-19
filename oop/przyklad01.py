def siema(x):
    print("Siema!")

class Osoba:
    imie = "nienazwany"
    nazwisko = "nieznane"
    waga = 0
    wzrost = 0
    def witaj(self, a):
        print(f"Witam {a}! {self}")
    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")
    def pokaz_bmi(self):
        print(f"Moje BMI: {self.bmi():.1f}")
    def bmi(self):
        return self.waga/self.wzrost**2
    def ustaw_imie(self, imie):
        self.imie = imie
    def ustaw_nazwisko(self, nazwisko):
        self.nazwisko = nazwisko

print(Osoba)
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

o4.waga = 60
o4.wzrost = 1.8

o4.pokaz_bmi()

if o4.bmi() < 20:
    print("Uuuuuu, niedożywiony.")
else:
    print("Wszystko w porządku")
