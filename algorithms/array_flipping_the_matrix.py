def flippingMatrix(matrix):
    n = len(matrix) // 2
    total_sum = 0

    for i in range(n):
        for j in range(n):
            total_sum += max(
                matrix[i][j],
                matrix[i][2 * n - 1 - j],
                matrix[2 * n - 1 - i][j],
                matrix[2 * n - 1 - i][2 * n - 1 - j]
            )
    print (i, j, '-', i, 2 * n - 1 - j, '-', 2 * n - 1 - i, j, 2 * n - 1 - i, 2 * n - 1 - j)
    return total_sum
