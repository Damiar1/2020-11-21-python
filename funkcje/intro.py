# Czy znamy jakieś funkcje?
# TAK!

# Najprostsza funkcja
def powitanie():
    print("Dzien dobry")
    print("...")
    print("Jaki piękny dzień")

powitanie()

print("--" * 20)

# Funkcja z jednym parametrem
def powitanie2(imie):
    x = 7
    print(f"Witaj, {imie}")
    print(f"Czyż nie jest piękny {pora_dnia}?")
    for i in range(3):
        print("Co nie?")

pora_dnia = "noc"
powitanie2("Mateusz")


print("--" * 20)
# Funkcja z jednym parametrem
def powitanie3(imie="nieznajomy"):
    print(f"Witaj, {imie}")

pora_dnia = "noc"
powitanie3("Mateusz")
powitanie3()

print("--" * 20)
# Funkcja zwracająca dwukrotność podanej liczby:

def dwukrotnosc_liczby(x):
    assert type(x) == int, f"Nieprawidłowy typ parametru w funkcji dwukrotnosc(): {type(x)}, oczekiwano: int"
#    print(f"Obliczam dwukrotność {x}")
#    print(2*x)
    return 2*x

def dwukrotnosc(x):
    return 2*x


# spodziewam sie wyniku 22
a = dwukrotnosc_liczby(7) + 8
print(a)

imiona = ["ala", "ola", "ela"]
b = dwukrotnosc(imiona)
print(b)

miesiace = "styczen luty marzec "
c = dwukrotnosc(miesiace)
print(c)


def znak_liczby(a):
    print(f"Sprawdzam znak liczby {a}")
    print(f"- sprawdzam czy mniejsza od zera...")
    if a < 0:
        print("Tak! Mniejsza od zera!")
        return -1
    print(f"- sprawdzam czy większa od zera...")
    if a > 0:
        print("Tak! Większa od zera!")
        return 1
    print("Sprawdzam czy może zero???")
    if a == 0:
        print("Tak! To zero!")
        return 0
    print("To się właściwie nie powinno wydarzyć...")

liczby = [1,3,5,0,-4,4,-99]

for n in liczby:
    print(f"{n} => {znak_liczby(n)}")
