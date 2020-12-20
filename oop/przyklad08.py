class Pracownik:
        def __init__(self, imie, nazwisko, stanowisko=None):
            self._imie = imie
            self._nazwisko = nazwisko
            self._stanowisko = stanowisko
            self._stawka = 0
            self._zarobione = 0.0
        def ustaw_stawke(self, stawka):
            self._stawka = stawka
        def pracuj(self, czas):
            print(f"{self._imie}: Pracuję {czas}h")
            self._zarobione += self._stawka * czas
        def raport(self):
            print(f"{self._imie} {self._nazwisko} ({self._stanowisko}): stawka {self._stawka:.2f}  zarobione: {self._zarobione:.2f}")
        def __repr__(self):
            return f"{self.__class__.__name__}{repr((self._imie, self._nazwisko, self._stanowisko))}"

class Menedzer:
    def __init__(self, imie, nazwisko, stanowisko=None):
        self._imie = imie
        self._nazwisko = nazwisko
        self._stanowisko = stanowisko
    def __repr__(self):
        return f"{self.__class__.__name__}{repr((self._imie, self._nazwisko, self._stanowisko))}"

p1 = Pracownik("Jan", "Kowalski")
p1.ustaw_stawke(47.50)
p1.pracuj(7.0)
p1.raport()
p1.pracuj(5.0)
p1.pracuj(4.0)
p1.pracuj(3.5)
p1.raport()

#p2 = Pracownik("Henryk", "Kowalczyk", "hydraulik")
#m1 = Menedzer("Andrzej", "Z")
#print(p1)

#pracownicy = [p1,p2,m1]

#print(pracownicy)
