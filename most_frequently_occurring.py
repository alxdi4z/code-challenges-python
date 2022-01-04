# Implement your function below.


def most_frequent(given_list: list):
    max_ocurrences = None
    number = None
    s = set()
    for i in given_list:
        if i not in s:
            s.add(i)
            if not max_ocurrences:
                max_ocurrences = given_list.count(i)
                number = i
                continue
            max = given_list.count(i)
            if max > max_ocurrences:
                max_ocurrences = max
                number = i

    return number


def most_frequent_2(given_list: list):
    count = {}
    for item in given_list:
        if item not in count.keys():
            count[item] = 1
        else:
            count[item] += 1
    if count:
        return max(count, key=count.get)


# NOTE: The following input values will be used for testing your solution.
# most_frequent(list1) should return 1
list1 = [1, 3, 1, 3, 2, 1]
# most_frequent(list2) should return 3
list2 = [3, 3, 1, 3, 2, 1]
# most_frequent(list3) should return None
list3 = []
# most_frequent(list4) should return 0
list4 = [0]
# most_frequent(list5) should return -1
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
