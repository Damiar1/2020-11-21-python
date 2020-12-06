uczniowie = [
  { "imie" : "Julian", "nazwisko" : "P.", "oceny" : "3 6 5 3 5 3 2 3 4 3 3" },
  { "imie" : "Agnieszka", "nazwisko" : "I.", "oceny" : "2 4 4 3 5 2 2 5 3 4 2" },
  { "imie" : "Magdalena", "nazwisko" : "M.", "oceny" : "4 4 3 3 3 4 4 3 4 4 3" },
  { "imie" : "Jacek", "nazwisko" : "L.", "oceny" : "5 3 3 4 4 5 2 4 3 4 3" },
  { "imie" : "Marta", "nazwisko" : "S.", "oceny" : "5 5 5 2 2 5 5 2 3 2 5" },
  { "imie" : "Jacek", "nazwisko" : "Z.", "oceny" : "2 5 5 3 5 3 3 3 5 4 3" },
  { "imie" : "Mateusz", "nazwisko" : "N.", "oceny" : "6 5 3 4 5 5 2 4 3 3 2" },
  { "imie" : "Karol", "nazwisko" : "I.", "oceny" : "3 4 3 3 3 3 3 4 3 4 4" },
  { "imie" : "Miriam", "nazwisko" : "L.", "oceny" : "4 3 2 4 3 4 3 3 3 4 4" },
  { "imie" : "Julian", "nazwisko" : "Y.", "oceny" : "4 4 4 4 3 4 3 4 3 3 4" },
  { "imie" : "Marta", "nazwisko" : "S.", "oceny" : "4 3 3 4 4 3 4 3 4 3 4" },
  { "imie" : "Mateusz", "nazwisko" : "N.", "oceny" : "3 3 5 6 6 5 4 6 4 3 3" },
  { "imie" : "Jacek", "nazwisko" : "J.", "oceny" : "3 5 2 4 4 1 3 5 4 2 3" },
  { "imie" : "Karol", "nazwisko" : "Q.", "oceny" : "4 4 2 4 3 6 5 2 4 6 5" },
  { "imie" : "Marta", "nazwisko" : "O.", "oceny" : "3 4 3 4 4 4 4 4 3 3 3" }
]

# TODO: zaimplementowac funkcje srednia_ucznia

for u in uczniowie:
    print(f"{u['imie']:15}  {srednia_ucznia(u)}")