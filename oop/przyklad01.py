def siema(x):
    print("Siema!")

class Osoba:
    def xxx(self):
        for i in range(3):
            print("x")
    def witaj(self, a):
        self.xxx()
        print(f"Witam {a}! {self}")

print(Osoba)
o1 = Osoba()
print(o1)

o2 = Osoba()
o3 = Osoba()
osoby = [o1, o2, o3]
print(osoby)

o4 = Osoba()
print(o4.witaj)
o4.witaj(600)

#siema()