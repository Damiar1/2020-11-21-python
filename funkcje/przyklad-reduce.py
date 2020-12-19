import functools

imiona = ["Ala", "Ula", "Basia", "Ela"]

# hint: zobacz najpierw błędny kod poniżej

x = functools.reduce(lambda a, b: a + len(b), imiona, 0)
# kroki reducyjne:
# 0 + len("Ala") => 3
# [ 3, "Ula", "Basia", "Ela" ]
# 3 + len("Ula") => 6
# [ 6, "Basia", "Ela" ]
# 6 + len("Basia") => 11
# [ 11, "Ela" ]
# 11 + len("Ela") => 14
# wynik: 14
print(x)


# To nie zadziała:
# po pierwszym kroku redukcyjnym:
# [6, "Basia", "Ela"]
# drugi krok redukcyjny jest niemożliwy
# bo nie da się policzyć len() do inta

x = functools.reduce(lambda a, b: len(a) + len(b), imiona)