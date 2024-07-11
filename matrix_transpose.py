def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))  # Should print the transposed matrix
