def opisz_pracownika(p):
    return f"{p['imie']} {p['nazwisko']} ({p['stanowisko'] if 'stanowisko' in p else '---'})"

def pokaz_pracownika(p, wciecie=0):
    print("    "* wciecie + opisz_pracownika(p) )
    if "pracownicy" in p:
        for pp in p['pracownicy']:
            pokaz_pracownika(pp, wciecie+1)

p1 = { "imie" : "Jan", "nazwisko" : "Kowalski", "stanowisko" : "elektryk" }
p2 = { "imie" : "Roman", "nazwisko" : "Kowalczyk", "stanowisko" : "hydraulik" }
sz1 = { "imie" : "Jacek", "nazwisko" : "Iksiński", "pracownicy" : [] }
p1['szef'] = sz1
p2['szef'] = sz1
sz1["pracownicy"].append( p1 )
sz1["pracownicy"].append( p2 )

p3 = { "imie" : "Barbara", "nazwisko" : "Kowalska", "stanowisko" : "sekretarka" }
p4 = { "imie" : "Krystyna", "nazwisko" : "Kowalczyk", "stanowisko" : "księgowa" }
sz2 = { "imie" : "Wanda", "nazwisko" : "Wandowska", "pracownicy" : [] }
p3['szef'] = sz2
p4['szef'] = sz2
sz2["pracownicy"].append( p3 )
sz2["pracownicy"].append( p4 )

pr = { "imie" : "XXX", "nazwisko" : "YYY", "pracownicy" : [] }
sz1['szef'] = pr
sz2['szef'] = pr
pr['pracownicy'].append( sz1 )
pr['pracownicy'].append( sz2 )

pokaz_pracownika(pr)
