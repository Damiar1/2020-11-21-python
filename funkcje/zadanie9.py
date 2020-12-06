p1 = { "imie" : "Jan", "nazwisko" : "Kowalski", "stanowisko" : "elektryk" }
p2 = { "imie" : "Roman", "nazwisko" : "Kowalczyk", "stanowisko" : "hydraulik" }
p3 = { "imie" : "Barbara", "nazwisko" : "Kowalska", "stanowisko" : "sekretarka" }
p4 = { "imie" : "Krystyna", "nazwisko" : "Kowalczyk", "stanowisko" : "księgowa" }
sz1 = { "imie" : "Jacek", "nazwisko" : "Iksiński", "pracownicy" : [] }
sz2 = { "imie" : "Wanda", "nazwisko" : "Wandowska", "pracownicy" : [] }
pr = { "imie" : "XXX", "nazwisko" : "YYY", "pracownicy" : [] }

def imie_p(p):
    return p['imie']

def nazwisko_p(p):
    return p['nazwisko']

def druga_litera_i(p):
    return p['imie'][1]

def dlugosc_imienia(p):
    return len(p['imie'])

wszyscy = [ pr, p1, p2, p3, p4, sz1, sz2 ]

wszyscy.sort(key=lambda p:len( p['imie'] ) )

for p in wszyscy:
    print(p)
