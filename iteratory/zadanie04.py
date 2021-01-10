# Mając listę wartości, policzyć wszystkie możliwe permutacje tej listy.

# np. A B C:
#
# A B C
# A C B
# B A C
# B C A
# C A B
# C B A

osoby = ('Andrzej', 'Basia', 'Czesław')

for x in permutacje(osoby):
    print(x)
