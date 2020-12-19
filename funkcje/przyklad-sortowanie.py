imiona = ["Asia", "Kasia", "Basia", "Zosia", "Krysia"]
print(f"Przed sortowaniem: {imiona}")
imiona.sort()
print(f"Po sortowaniu: {imiona}")

rozmaitosci = [4, "Test", False, (4,6,9), [1,3,3], "koniec"]
rozmaitosci.sort() # to się nie uda, bo lista zawiera elementy róznych typów (niemożliwe do porównania)