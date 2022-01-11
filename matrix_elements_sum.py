def matrixElementsSum(matrix: list) -> float:
    total = 0
    cursed = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i - 1 >= 0:
                if j in cursed:
                    continue
            if matrix[i][j] == 0 and j not in cursed:
                cursed.add(j)
            if matrix[i][j] > 0:
                total += matrix[i][j]
    return total


a1 = [[1, 1, 1, 0],
      [0, 5, 0, 1],
      [2, 1, 3, 10]]

print(matrixElementsSum(a1))
