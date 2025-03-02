memo1 = {0: 0, 1: 1}
counter1 = 0


def fib_top_down(n):  # Top Down
    global counter1
    counter1 += 1
    # if n == 0 or n == 1:
    #     return n
    if n in memo1:
        return memo1[n]
    else:
        fib_n = fib_top_down(n - 1) + fib_top_down(n - 2)
        memo1[n] = fib_n
        return fib_n


n = 35
print(f"Fib of {n} is {fib_top_down(n)}")
print(f"Counter={counter1}")
print(f"Memo1: {memo1}")

memo2 = {0: 0, 1: 1}
counter2 = 0


def fib_bottom_up(n):
    global counter2
    for index in range(2, n + 1):
        counter2 += 1
        next_fib = memo2[index - 1] + memo2[index - 2]
        memo2[index] = next_fib
    return memo2[n]


print(f"Fib of {n} is {fib_bottom_up(n)}")
print(f"Counter={counter2}")
print(f"Memo2: {memo2}")