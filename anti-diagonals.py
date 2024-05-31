def print_antidiagonals(matrix):
    m = len(matrix)
    n = len(matrix[0])

    # Iterate over the anti-diagonals below the main diagonal
    for i in range(m):
        row = i
        col = 0
        while row >= 0 and col < n:
            print(matrix[row][col], end=" ")
            row -= 1
            col += 1
        print()

    # Iterate over the anti-diagonals above the main diagonal
    for j in range(1, n):
        col = j
        row = m - 1
        while col < n and row >= 0:
            print(matrix[row][col], end=" ")
            row -= 1
            col += 1
        print()

# Example usage
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

if __name__ == "__main__":
    print("Anti-diagonal elements:")
    print_antidiagonals(matrix)
