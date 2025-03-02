# https://www.bigocheatsheet.com/
# Examples:

def func1(n):  # O(1)
    r = (n + n) * n ** 2
    print(r)


def func2(n):  # O(log(n))
    i = 1
    while i < n:
        print(i)
        i *= 2


def func3(n):  # O(n)
    for i in range(n):
        print(n)


def func4(n):  # O(n.log(n))
    for i in range(n):
        j = 1
        while j < n:
            print(i, j)
            j *= 2


def func5(n):  # O(n^2)
    for i in range(n):
        for j in range(n):
            print(i, j)


def func6(n):  # O(2^n)
    if n == 0 or n == 1:
        return n
    else:
        r = func6(n - 1) + func6(n - 2)
        print(r)
        return r


def func7(n):  # O(n!)
    for i in range(n):
        func7(n - 1)
