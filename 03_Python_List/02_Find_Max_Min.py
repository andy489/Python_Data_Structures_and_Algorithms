def find_max_min(my_list):
    maximum = minimum = my_list[0]
    for num in my_list:
        if num > maximum:
            maximum = num
        elif num < minimum:
            minimum = num
    return maximum, minimum


print(find_max_min([5, 3, 8, 1, 6, 9]))

"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
"""