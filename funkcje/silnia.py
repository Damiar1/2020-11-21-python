def silnia(n):
    print(f"Obliczam silnia({n})")
    if n == 0:
        return 1
    else:
        return n*silnia(n-1)

def silnia2(n):
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

print( silnia(400) )
print( silnia2(400) )
