liczby = [3, 5, 10, 11, 15, 1, 23, 2, 3, 10, 0, 4, 17, 7]

#def trzykrotnosc(x):
#    return 3*x

#liczby3 = list(map(trzykrotnosc, liczby))

liczby3 = list(map(lambda x:3*x, liczby))

liczby3bis = [ 3*x for x in liczby ]

print(liczby3)
print(liczby3bis)
