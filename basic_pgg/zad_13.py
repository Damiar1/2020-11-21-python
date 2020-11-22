"""
Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o rozmiarach 10 na 10.
Użytkownik może wprowadzać komendy zmieniające położenie postaci.
Po każdym ruchu użytkownik powinien otrzymywać informację o tym, czy zmierza dobrym kierunku.
Wyjście poza planszę oznacza koniec gry.
Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na dojście do celu.
Dodatkowo:
- po wykonaniu większej liczby kroków niż dwukrotność minimalnej liczby kroków umieść skarb w nowym miejscu,
- z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku.
"""

gracz_x = 5
gracz_y = 5

skarb_x = 7
skarb_y = 7

liczba_krokow = 0

while True:
    print(f'Twoja pozycja: x={gracz_x} y={gracz_y}')
    kierunek = input("Podaj kierunek (w, s, a, d): ")

    if kierunek == 'w':
        gracz_y += 1
    elif kierunek == 's':
        gracz_y -= 1
    elif kierunek == 'a':
        gracz_x -= 1
    elif kierunek == 'd':
        gracz_x += 1
    else:
        print("Niepoprawny ruch!")
        continue

    liczba_krokow += 1

    # if gracz_x < 0 or gracz_x > 10 or gracz_y < 0 or gracz_y > 10:
    if not (0 <= gracz_x <= 10) or not (0 <= gracz_y <= 10):
        print("Jestes poza plansza! GAME OVER!")
        # break # to przerwie petle, po petli nic nie ma, wiec jest OK
        exit() # zamknie caly program, jezeli cos jest po petli while to sie nie wykona!

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print('Brawo! Znalazles skarb!!!')
        print(f'Liczba krokow to {liczba_krokow}')
        exit()
