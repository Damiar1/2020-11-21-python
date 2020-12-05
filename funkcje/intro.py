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

