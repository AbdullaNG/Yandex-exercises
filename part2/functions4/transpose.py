def transpose(matrix):
    m = len(matrix[0])
    n = len(matrix)
    lt = []
    for j in range(m):
        tp = []
        for i in range(n):
            tp = tp + [matrix[i][j]]
        lt += [tp]

    matrix[:] = lt