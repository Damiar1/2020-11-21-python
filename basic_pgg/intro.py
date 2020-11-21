# to jest komentarz jednolinijkowy
# Uruchomienie na Macu: ctrl+shift+r
# Uruchomienie na Windowsie: ctrl+shift+f10
print("Hello world!")

# Typy danych
# napis, string - str
# definiujemy w " albo '
print('Hello world!')
print("Hello world!")

print("Ksiazka 'Pan Tadeusz' jest fajna!")
print('Ksiazka "Pan Tadeusz" jest fajna')
print("Ksiazka \"Pan Tadeusz\" jest fajna") # trzeba wyeskejpowac \"
print('Ksiazka \'Pan Tadeusz\' jest fajna')

# int - liczby całkowite
# int - ma nieograniczoną precyzje
print(10)

# float
print(3.14)
print(3.0)
print(3.)
print(0.5)
print(.5)

print(type(3.0)) # float
print(type(3)) # int

print(type(float(3))) # zmiana typu / rzutowanie

# bool
# typ danych, który posiada dwie wartości: prawda i fałsz
print(True)
print(False)

print(type(True))
print(type(False))

# wartość pusta
# w innych językach zwykle jest to null
print(None)

print(type(10)) # int
print(type(10.0)) # float
print(type("10")) # str

print(10 + 5) # 15
print("10" + "5") # 105 - tekst a nie liczba!

# Operatory
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5) # int / int -> float!
print(10 // 3) # dzielenie calkowitoliczbowe
print(type(10 // 3)) # dzielenie calkowitoliczbowe, dostajemy int
print(10 % 3) # reszta z dzielenia, modulo
print(10 ** 3) # potegowanie

print("Ala " + "ma kota") # konkatenacja, laczenie napisow
print("Ala" * 10) # powielamy napis X razy


# print("Ala ma lat: " + 10) # nie zadziala i bedzie blad
print("Ala ma lat: " + str(10)) # przerabiasz int na string
print("Ala ma lat: " + str(10.5))

# literal - wartosc wpisana bezposrednio w kodzie

# żąśźćęńłó - w komentarzach mogą być polskie znaki

print('Ala ma kota')
print("Ala ma\nkota")
print("""Ala ma kota
Kot ma kompilator
jest nowy wiersz""")

print('''Pierwsza linijka
Druga linijka
Trzecia linijka
''')

# zmienna
imie = 'Piotr' # nazwa_zmiennej = wartosc

print(imie)

imie = 44

print(imie)

imie = "Tomek"
print(imie)

# nazywanie zmiennych: PEP8 https://www.python.org/dev/peps/pep-0008

adres_zamieszkania = "ul. Polna 10, 12-345 Warszawa"

napis_z_polskimi_znakami = "Zażółć gęślą jaźń"
print(napis_z_polskimi_znakami)
