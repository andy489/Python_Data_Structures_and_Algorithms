from collections import deque


def reverse_string(rand_string):
    stack = deque()
    for char in rand_string:
        stack.append(char)
    reversed_string = ""
    while len(stack) > 0:
        reversed_string += stack.pop()
    return reversed_string


my_string = 'hello'

print(reverse_string(my_string))

"""
    EXPECTED OUTPUT:
    ----------------
    olleh
"""
