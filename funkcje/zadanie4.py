osoby = [
    { "id":"Michał", "zarobki": 4000, "dg":True },
    { "id":"Karol", "zarobki": 1000, "dg":False },
    { "id":"Andrzej", "zarobki": 2000, "dg":False },
    { "id":"Piotr", "zarobki": 6005, "dg":True },
    { "id":"Zygmunt", "zarobki": 6005, "dg":False },
    { "id":"Zbigniew", "zarobki": 7000, "dg":True }
]

def podatek_liniowy(kwota):
    return 0.15 * kwota

def nowy_podatek_liniowy(stawka):
    def p(kwota):
        return stawka * kwota
    return p

def zwolnienie_z_podatku(kwota):
    return 0

def podatek_2p(kwota):
    if kwota < 3000:
        return 0.1 * kwota
    else:
        return 300 + 0.2 * (kwota - 3000)

def ktory_podatek(osoba):
    if osoba['id'][0] == 'Z':
        return nowy_podatek_liniowy(0.11)
    if osoba['dg']:
        return podatek_liniowy
    if osoba['zarobki'] < 1900:
        return zwolnienie_z_podatku
    return podatek_2p

for o in osoby:
    podatek = ktory_podatek(o)
    kwota_podatku = podatek(o['zarobki'])

    print(f"{o['id']:12} : {o['zarobki']:10}  {kwota_podatku:10}   {podatek}")
