# Kolekcje

# Tupla, krotka, tuple

#    0   1   2 - indeks
a = (10, 20, 30)
print(a)
print( a[1] ) # 20
print( a[0] ) # 10

print('-'*30)

#    0  1    2              3 - indeks
b = (1, 2.5, "Ala ma kota", True)
print(b[0])
print(b[1])
print(b[2])
print(b[3])

# b[0] = 100 # TypeError: 'tuple' object does not support item assignment

#     0       1                2
c = ( (1, 2), ('a', 'b', 'c'), (True, False) )
#      0  1    0    1    2      0     1

print(c[0][1])
print(c[1][2])

print(type(c)) # tuple
print('-'*30)

# jak stworzyć tuple, ktora ma tylko jeden element?
d = (100,) # to , a nie nawiasy powoduja, ze python tworzy tuple!
print(type(d))

print('-'*30)

#          0    1    2    3    4    5    6    7    8
literki = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i')

print(literki[0])
print(literki[3])
# [a:b] - lewostronnie domkniety, prawostronnie otwarty
print(literki[1:3]) # b, c
print(literki[1:9]) # 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'
print(literki[3:]) # 'd', 'e', 'f', 'g', 'h', 'i'
print(literki[-1]) # 'i'
print(literki[-3:]) # 'g', 'h', 'i'
print(literki[-3:-2]) # g
print(literki[5:-2]) # f, g - bo ostatni nie wchodzi!
print(literki[:-1]) # 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'
print(literki[:])
print(literki[-2:3]) # pusta tupla
# od : do : co ile
print(literki[::2]) # co drugi element, 'a', 'c', 'e', 'g', 'i'
print(literki[::-1]) # 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a'

print('-'*30)

# ile tupla ma elementow?
print(len(literki))

# czy element znajduje sie w tupli
print('a' in literki)

liczby = (10, 20, 30, 40, 50)

print(max(liczby))
print(min(liczby))
print(sum(liczby))

i = (1, 2, 3)
j = (4, 5, 6)

k = i + j
print(k)

l = i * 5
print(l)


