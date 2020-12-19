import functools

osoba1 = {"imie":"Xawery", "wzrost":1.81, "waga":72 }
osoba2 = {"imie":"Zdzisław", "wzrost":1.61, "waga":92 }
osoba3 = {"imie":"Zygmunt", "wzrost":1.91, "waga":71 }
osoba4 = {"imie":"Alojzy", "wzrost":1.72, "waga":93 }

osoby = [ osoba1, osoba2, osoba3, osoba4 ]

# wypisz osoby posortowane wg wzrostu
osoby.sort(key=lambda osoba:osoba["wzrost"])

# wypisz osoby posortowane wg wzrostu (od najwyższego)
osoby.sort(key=lambda osoba:-osoba["wzrost"])
osoby.sort(key=lambda osoba:osoba["wzrost"], reverse=True)

# wypisz osoby posortowane wg BMI
osoby.sort(key=lambda o:o['waga']/(o['wzrost']**2))

for o in osoby:
    print(o)

# przekształć listę osób na listę stringów w formacie:
# imie (BMI)
# np. [ "Maks (24.6)", ...itd]

#def formatuj_osobe(o):
#    return f"{o['imie']} ({o['waga']/(o['wzrost']**2):.1f})"

#osoby_bmi = list(map(formatuj_osobe,osoby))
osoby_bmi = list(map(lambda o:f"{o['imie']} ({o['waga']/(o['wzrost']**2):.1f})", osoby))
print(osoby_bmi)

# za pomocą filter() stwórz listę osób z niedowagą (BMI<20)
osoby_niedowaga = list(filter(lambda o:o['waga']/(o['wzrost']**2)<20, osoby))
print(osoby_niedowaga)

# za pomoca reduce() policzyć sumaryczną wagę wszystkich osób
sumaryczna_waga = functools.reduce(lambda w, o: w + o['waga'], osoby, 0 )

# alternatywne rozwiązanie, bez reduce() tylko z sum()
sw2 = sum([ o['waga'] for o in osoby ])

print(sumaryczna_waga)
print(sw2)

# za pomocą reduce() stworzyć łańcuch tekstowy zawierający pierwsze litery imion wszystkich osób np. "XZZA"
inicjaly = functools.reduce(lambda a, b: a + b['imie'][0], osoby, "")
print(inicjaly)

# alternatywne rozwiązanie, bez reduce() tylko z .join()
in2 = "".join([ o['imie'][0] for o in osoby ])
print(in2)
