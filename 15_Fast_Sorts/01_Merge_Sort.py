def merge_sort(my_list): # O(n log(n))
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    return merge(left, right)

def merge(list1, list2):
    combined = [None] * (len(list1) + len(list2))
    i = j = k = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined[k] = list1[i]
            i += 1
        else:
            combined[k] = list2[j]
            j += 1
        k += 1
    while i < len(list1):
        combined[k] = list1[i]
        i += 1
        k += 1
    while j < len(list2):
        combined[k] = list2[j]
        j += 1
        k += 1
    return combined

original_list = [1,8,2,10,47,3,8]
sorted_list = merge_sort(original_list)

print(f"Original list: {original_list}")
print(f"Sorted list: {sorted_list}")
