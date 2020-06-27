# https://leetcode.com/problems/rotate-image/
'''
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
'''


def rotateInplace(matrix):
    for i in range(N):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(N):
        matrix[i].reverse()


def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    mat2 = []
    for i in zip(*matrix[:: -1]):
        mat2.append(list(i))
    # Inplace workaround
    matrix.clear()
    matrix.extend(mat2)


if __name__ == "__main__":
    N = 3
    matrix = [[i+(N*j)+1 for i in range(0, N)] for j in range(0, N)]
    print(f'Matrix\n', *matrix, sep='\n')

    rotateInplace(matrix)
    print(f'\nMatrix Rotated\n', *matrix, sep='\n')
