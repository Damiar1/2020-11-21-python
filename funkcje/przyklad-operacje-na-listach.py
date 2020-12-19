import functools

# aby móc wołać po prostu reduce() zamiast functools.reduce()
# from functools import *
# from functools import reduce

liczby = [3, 5, 10, 11, 15, 1, 23, 2, 3, 10, 2, 4, 17, 7]

#def trzykrotnosc(x):
#    return 3*x

#liczby3 = list(map(trzykrotnosc, liczby))
liczby3 = list(map(lambda x:3*x, liczby))
liczby3bis = [ 3*x for x in liczby ]
print(liczby3)
print(liczby3bis)

# tylko większe równe od 10
#def ge10(x):
#    return x >= 10

#liczby10 = list(filter(ge10,liczby))
liczby10 = list(filter(lambda x:x>=10, liczby))
liczby10bis = [ x for x in liczby if x>=10 ]
print(liczby10)
print(liczby10bis)

#def mnoz(a, b):
#    return a*b

#produkt = functools.reduce(mnoz,liczby)
produkt = functools.reduce(lambda a, b: a*b, liczby)
suma = functools.reduce(lambda a, b: a+b, liczby)
najwieksza = functools.reduce(lambda a, b: a if a > b else b, liczby)

print(produkt)
print(suma)
print(najwieksza)

imiona = [ "Ala", "Ola", "Ela"]

il1 = functools.reduce( lambda a,b: a + " " + b, imiona, "Imiona:")
il2 = functools.reduce( lambda a,b: a + " " + b, ["Imiona:"] + imiona )
print(il1)
print(il2)
