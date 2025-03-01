def item_in_common_slow(list1, list2):  # O(n^2)
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


def item_in_common(list1, list2):  # O(n)
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True

    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common_slow(list1, list2))
print(item_in_common_fast(list1, list2))
