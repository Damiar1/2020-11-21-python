def drukuj_swiadectwo(
        imie="##IMIE##",
        nazwisko="##NAZWISKO##",
        klasa="KLASA",
        oceny={"PRZEDMIOT1":0,"PRZEDMIOT2":0}
):
    print(f"-----SWIADECTWO-----")
    print(f"     imie: {imie}")
    print(f" nazwisko: {nazwisko}")
    print(f"UKONCZYL KLASE {klasa}")
    for przedmiot, ocena in oceny.items():
        print(f"{przedmiot}: {ocena}")
    print(f"-----KONIEC-----")


drukuj_swiadectwo(nazwisko="Kowalski", imie="Jan")

sw1 = {"imie":"Janusz", "nazwisko":"Jjj", "klasa":7, "oceny" : {"matematyka":5,"polski":4}}

drukuj_swiadectwo( **sw1 )
