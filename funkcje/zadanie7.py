"""
Napisać funkcję splaszcz(lista),
która zamieni listę z zagnieżdżonymi listami, na zwykłą listę liczb.

"""

x = [ 5, 6, 76, 45, [ 234, 43, 34, [ 43, [[43]] ], [34, [[43]]], [43] ], 100 ]

def splaszcz(lista):
    wynik = []
    for e in lista:
        if type(e) == list:
            wynik += splaszcz(e)
        else:
            wynik += [ e ]
    return wynik

x2 = splaszcz( x )
print(x2)

# chcemy uzyskać:
# [ 5, 6, 76, 45, 234, 43, 34, 43, 43, 34, 43, 43, 100 ]

