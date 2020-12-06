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

def przelicz_C_na_K(t):
    return t + 273.15

def przelicz_K_na_C(t):
    return t - 273.15

def przelicz_C_na_F(t):
    return 1.8 * t + 32

def przelicz_F_na_C(t):
    return (t - 32)/1.8

def przelicz_K_na_F(t):
    return przelicz_C_na_F(przelicz_K_na_C(t))

def przelicz_F_na_K(t):
    return przelicz_C_na_K(przelicz_F_na_C(t))


temperatury = [ -50, -20, -10, -1, 0, 1, 5, 15, 25, 70, 100, 200, 300 ]

for temperatura in temperatury:
    print(f"{temperatura:10.2f}C = {przelicz_C_na_F(temperatura):10.2f}F = {przelicz_C_na_K(temperatura):10.2f}K")