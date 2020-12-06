uczniowie = [
  { "imie" : "Julian", "nazwisko" : "P.", "oceny" : "3 6 5 3 5 3 2 3 4 3 3" },
  { "imie" : "Agnieszka", "nazwisko" : "I.", "oceny" : "6 4 4 6 5 6 2 6 6 6 2" },
  { "imie" : "Magdalena", "nazwisko" : "M.", "oceny" : "4 4 3 3 3 4 4 3 4 4 3" },
  { "imie" : "Jacek", "nazwisko" : "L.", "oceny" : "5 3 3 4 4 5 2 4 3 4 3" },
  { "imie" : "Marta", "nazwisko" : "S.", "oceny" : "5 5 5 2 2 5 5 2 3 2 5" },
  { "imie" : "Jacek", "nazwisko" : "Z.", "oceny" : "2 5 5 3 5 3 3 3 5 4 3" },
  { "imie" : "Mateusz", "nazwisko" : "N.", "oceny" : "6 5 6 5 5 5 6 4 5 5 6" },
  { "imie" : "Karol", "nazwisko" : "I.", "oceny" : "3 4 3 3 3 3 3 4 3 4 4" },
  { "imie" : "Miriam", "nazwisko" : "L.", "oceny" : "4 3 2 4 3 4 3 3 3 4 4" },
  { "imie" : "Julian", "nazwisko" : "Y.", "oceny" : "4 6 4 5 6 4 6 5 6 6 4" },
  { "imie" : "Marta", "nazwisko" : "S.", "oceny" : "4 3 3 4 4 3 4 3 4 3 4" },
  { "imie" : "Mateusz", "nazwisko" : "N.", "oceny" : "3 3 5 6 6 5 4 6 4 3 3" },
  { "imie" : "Jacek", "nazwisko" : "J.", "oceny" : "3 5 2 4 4 1 3 5 4 2 3" },
  { "imie" : "Karol", "nazwisko" : "Q.", "oceny" : "4 4 2 4 3 6 5 2 4 6 5" },
  { "imie" : "Marta", "nazwisko" : "O.", "oceny" : "3 4 3 4 4 4 4 4 3 3 3" }
]

def srednia_ocen(oceny):
  return sum(oceny) / len(oceny)

def srednia_ucznia(uczen):
  return srednia_ocen([int(o) for o in uczen['oceny'].split()])

def imie_i_nazwisko_ucznia(uczen):
  return f"{uczen['imie']} {uczen['nazwisko']}"

def podsumowanie(uczen):
  return imie_i_nazwisko_ucznia(uczen), srednia_ucznia(uczen)

def czy_czerwony_pasek(uczen):
  if srednia_ucznia(uczen) >= 4.75:
    return True
  return False

for u in uczniowie:
    imie_n, sr = podsumowanie(u)
    print(f"{imie_n:15}  {sr}")
    print(czy_czerwony_pasek(u))

najwyzsza_srednia = max( srednia_ucznia(u) for u in uczniowie )
print(najwyzsza_srednia)
