"""
Moduł służący do różnych zabaw z alfabetem.
"""

litery = 'ABCDEFG'

def abecadlo(n: int) -> str:
    """
    Funkcja zwraca alfabet powtórzony n razy
    :param n: ile razy powtórzyć alfabet
    :return:
    """
    return 'abcdefghijklmnopqrstuvwxyz' * n

class Abc():
    """
    Klasa reprezentująca abecadło.
    """
    def __init__(self, x):
        """
        Cokolwiek.
        :param x: ostatnia litera
        """
        self.x = x

