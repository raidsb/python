def flipping_matrix(matrix):
    n = len(matrix) // 2
    total_sum = 0

    for i in range(n):
        for j in range(n):
            # Indices in the upper-left quadrant
            upper_left_indices = (i, j)

            # Corresponding indices in the other three quadrants
            upper_right_indices = (i, 2 * n - 1 - j)
            lower_left_indices = (2 * n - 1 - i, j)
            lower_right_indices = (2 * n - 1 - i, 2 * n - 1 - j)

            # Find the maximum element from the four corresponding positions
            max_value = max(
                matrix[upper_left_indices[0]][upper_left_indices[1]],
                matrix[upper_right_indices[0]][upper_right_indices[1]],
                matrix[lower_left_indices[0]][lower_left_indices[1]],
                matrix[lower_right_indices[0]][lower_right_indices[1]]
            )

            # Print the indices being compared
            print(f"Indices: {upper_left_indices}, {upper_right_indices}, {lower_left_indices}, {lower_right_indices}")

            total_sum += max_value

    return total_sum

# Example usage
matrix = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108]
]

result = flipping_matrix(matrix)
print("Total Sum:", result)


