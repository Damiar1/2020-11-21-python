import random

def wybierz_operacje(nazwa):
    print(f"Wybieram operacja o nazwie: {nazwa}")
    fd = lambda x:2*x
    ft = lambda x:3*x
    fo = lambda x:1/x
    if nazwa == "dwukrotnosc":
        return fd
    if nazwa == "trzykrotnosc":
        return ft
    if nazwa == "odwrotnosc":
        return fo
    if nazwa == "losowa":
        return random.choice([fd,ft,fo])


print(wybierz_operacje)
operacja = wybierz_operacje("dwukrotnosc")
print(operacja)

liczba = 10
wynik = operacja(liczba)
print(wynik)

liczby = [1, 10, 100, 200, 700]

# te dwa rozwiązania różnią się wydajnością, ale ostatecznie nie różnią się wynikiem
przekonwertowane=list(map(wybierz_operacje("trzykrotnosc"), liczby))
print(przekonwertowane)

przekonwertowane2 = [ wybierz_operacje("trzykrotnosc")(x) for x in liczby ]
print(przekonwertowane2)

# tutaj jest już zupełnie inna zasada działania
# wszystkie liczby są przekształcane tą samą funkcją
przekonwertowane=list(map(wybierz_operacje("losowa"), liczby))
print(przekonwertowane)
# każda liczba ma kazdorazowo losowaną funkcję
przekonwertowane2 = [ wybierz_operacje("losowa")(x) for x in liczby ]
print(przekonwertowane2)

