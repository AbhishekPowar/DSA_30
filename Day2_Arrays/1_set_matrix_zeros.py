# https://leetcode.com/problems/set-matrix-zeroes/

# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]


def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    r = set()
    c = set()
    matrix_len = len(matrix)
    row_len = len(matrix[0])
    for i in range(matrix_len):
        for j in range(row_len):
            if matrix[i][j] == 0:
                r.add(i)
                c.add(j)

    for i in r:
        for j in range(row_len):
            matrix[i][j] = 0

    for i in range(matrix_len):
        for j in c:
            matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    print(*matrix, sep='\n')
    setZeroes(matrix)
    print(*matrix, sep='\n')
