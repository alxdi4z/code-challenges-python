# Common Elements in Two Sorted Array

# not a good solution
def common_elements(list1, list2):
    used = set()
    result = []
    for item in list1:
        if item not in used:
            used.add(item)
            if item in list2:
                result.append(item)
    return result


def common_elements2(list1, list2):
    p1 = 0
    p2 = 0
    result = []

    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            p1 += 1

    return result


list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]
# common_elements(list_a1, list_a2) should return [1, 4, 9] (a list).

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
# common_elements(list_b1, list_b2) should return [1, 2, 9, 10, 12] (a list).

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# common_elements(list_b1, list_b2) should return [] (an empty list).

print(common_elements2(list_a1, list_a2))
print(common_elements2(list_b1, list_b2))
print(common_elements2(list_c1, list_c2))
