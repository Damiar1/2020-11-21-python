# zaimplementowac funkcję fib(n)
# obliczającą n-tą wartość w ciągu Fibonacciego
# metodą rekurencyjną
#
# np. fib(0) -> 0
# fib(1) -> 1
# fib(2) -> 1
# fib(3) -> 2
# fib(4) -> 3
# fib(5) -> 5
# fib(6) -> 8 itd

def fib(n):
    print(f"Obliczam {n}. element ciągu Fibonacciego")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(7))

