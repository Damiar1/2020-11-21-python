"""
Napisać funkcję splaszcz(lista),
która zamieni listę z zagnieżdżonymi listami, na zwykłą listę liczb.

"""

x = [ 5, 6, 76, 45, [ 234, 43, 34, [ 43, 43 ], [34, 43], [43] ], 100 ]

# TODO
# def splaszcz(lista):
#

x2 = splaszcz( x )
print(x2)

# chcemy uzyskać:
# [ 5, 6, 76, 45, 234, 43, 34, 43, 43, 34, 43, 43, 100 ]

