def almostIncreasingSequence(sequence: list) -> bool:
    changes = 0
    if len(sequence) == 2:
        return True
    for i in range(len(sequence)):
        if i + 1 < len(sequence) and sequence[i+1] <= sequence[i]:
            changes += 1
            skipNeighbor = i + \
                2 < len(sequence) and sequence[i + 2] <= sequence[i]
            skipBack = i - 1 >= 0 and sequence[i+1] <= sequence[i - 1]
            if skipNeighbor and skipBack or changes >= 2:
                return False

    return True


def almostIncreasingSequence2(sequence: list) -> bool:
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True


a1 = [1, 3, 2, 1]  # should return False
a2 = [1, 3, 2]  # should return True
a3 = [1, 2, 3, 4, 3, 6]  # should return True
a4 = [3, 6, 5, 8, 10, 20, 15]  # should return False
a5 = [123, -17, -5, 1, 2, 3, 12, 43, 45]  # should return True
a6 = [1, 2, 1, 2]  # should return False
a7 = [1, 1, 2, 3, 4, 4]  # should return False

print(almostIncreasingSequence2(a1))
# print(almostIncreasingSequence(a2))
# print(almostIncreasingSequence(a3))
# print(almostIncreasingSequence(a4))
# print(almostIncreasingSequence(a5))
# print(almostIncreasingSequence(a6))
# print(almostIncreasingSequence(a7))
