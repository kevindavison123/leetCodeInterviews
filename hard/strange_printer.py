#There is a strange printer with the following two special requirements:
#
#    On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
#    Once the printer has used a color for the above operation, the same color cannot be used again.
#
#You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the position (row, col) of the grid.
#
#Return true if it is possible to print the matrix targetGrid, otherwise, return false.


def isPrintable(targetGrid):
    m, n = len(targetGrid), len(targetGrid[0])
    colors = {}

    # Step 1: Find the bounding box for each color
    for i in range(m):
        for j in range(n):
            color = targetGrid[i][j]
            if color not in colors:
                colors[color] = [i, j, i, j]  # min_row, min_col, max_row, max_col
            else:
                colors[color][0] = min(colors[color][0], i)
                colors[color][1] = min(colors[color][1], j)
                colors[color][2] = max(colors[color][2], i)
                colors[color][3] = max(colors[color][3], j)




    for i in range(m):
        for j in range(n):
            color = targetGrid[i][j]
            if color not in colors:
                colors[color] = [i, j, i, j]  # min_row, min_col, max_row, max_col
            else:
                colors[color][0] = min(colors[color][0], i)
                colors[color][1] = min(colors[color][1], j)
                colors[color][2] = max(colors[color][2], i)
                colors[color][3] = max(colors[color][3], j)

    # Step 2: Check if a color can be printed
    def can_print(color):
        min_row, min_col, max_row, max_col = colors[color]
        for i in range(min_row, max_row + 1):
            for j in range(min_col, max_col + 1):
                if targetGrid[i][j] != color and targetGrid[i][j] != 0:
                    return False
        return True

    # Step 3: Try to print colors iteratively
    printed = set()
    while len(printed) < len(colors):
        progress = False
        for color in colors:
            if color not in printed and can_print(color):
                min_row, min_col, max_row, max_col = colors[color]
                for i in range(min_row, max_row + 1):
                    for j in range(min_col, max_col + 1):
                        targetGrid[i][j] = 0  # Mark as printed
                printed.add(color)
                progress = True
        if not progress:
            return False

    return True




print(isPrintable([[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]))
print(isPrintable([[1,2,1],[2,1,2],[1,2,1]]))