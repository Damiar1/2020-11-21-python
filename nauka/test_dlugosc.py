from .geometria import Dlugosc

# testy pytest
# instalacja pytest: py -m pip install pytest

# uruchomienie testów:
#  pytest
# wygenerowanie raportu HTML
#  pytest --html=plik.html

def test_sprawdz_konstruktor_liczba_int_i_jednostka_str():
    d1 = Dlugosc(1, 'm')
    assert type(d1) == Dlugosc

def test__wartosc_z_jednostka_liczba_z_jednostka_str_typ_zwracany():
    assert type(Dlugosc._wartosc_z_jednostka("1m")) == tuple

def test__wartosc_z_jednostka_liczba_z_jednostka_str_dlugosc_krotki():
    assert len(Dlugosc._wartosc_z_jednostka("1m")) == 2

def test__wartosc_z_jednostka_liczba_z_jednostka_str_zawartosc_krotki():
    assert Dlugosc._wartosc_z_jednostka("1m") == (1, "m")

def test__xyz():
    d1 = Dlugosc(1, 'm')
    d2 = Dlugosc('1m')
    assert d1 == d2

