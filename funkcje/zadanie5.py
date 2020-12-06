"""
Napisać 6 funkcji przeliczających temperatury:
- z C na K
- z K na C
- z C na F
- z F na C
- z K na F
- z F na K
"""

# def przelicz_C_na_K(t):
# itd

def funkcja_liniowa(a, b):
    def f(x):
        return a*x+b
    return f

def przelicz_C_na_K(t):
    return funkcja_liniowa(1, 273.15)(t)

def przelicz_K_na_C(t):
    return funkcja_liniowa(1, -273.15)(t)

def przelicz_C_na_F(t):
    return funkcja_liniowa(1.8, 32)(t)

def przelicz_F_na_C(t):
    return funkcja_liniowa(5/9, -5/9*32)(t)

def przelicz_K_na_F(t):
    return przelicz_C_na_F(przelicz_K_na_C(t))

def przelicz_F_na_K(t):
    return przelicz_C_na_K(przelicz_F_na_C(t))

temperatury = [ -50, -20, -10, -1, 0, 1, 5, 15, 25, 70, 100, 200, 300 ]

for temperatura in temperatury:
    print(f"{temperatura:10.2f}C = {przelicz_C_na_F(temperatura):10.2f}F = {przelicz_C_na_K(temperatura):10.2f}K")

temperaturyF = [ -10, 0, 10, 32, 60, 212 ]

for temperatura in temperaturyF:
    print(f"{temperatura:10.2f}F = {przelicz_F_na_C(temperatura):10.2f}C")