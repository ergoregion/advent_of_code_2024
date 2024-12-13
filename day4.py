import numpy as np

result = 0

txt = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''

with open('data/day4data', 'r') as file:
    txt = file.read()


def is_an_xmas(arr, i, j, delta):
    if (i + 3 * delta[0] < 0):
        return False
    if (j + 3 * delta[1] < 0):
        return False

    if (i + 3 * delta[0] > len(arr)):
        return False
    if (j + 3 * delta[1] > len(arr[0])):
        return False

    if (arr[i][j] != 'X'):
        return False
    if (arr[i + delta[0]][j + delta[1]] != 'M'):
        return False
    if (arr[i + 2 * delta[0]][j + 2 * delta[1]] != 'A'):
        return False
    if (arr[i + 3 * delta[0]][j + 3 * delta[1]] != 'S'):
        return False

    return True


delta_options = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
arr = [list(x) for x in txt.splitlines()]

print(arr)

for delta_option in delta_options:
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            try:
                if (is_an_xmas(arr, i, j, delta_option)):
                    result += 1
            except:
                pass

print(result)


class FivePointStencil:
    def __init__(self):
        pass

    def __call__(self, arr, i, j):
        return self._right_diagonal(arr, i, j) and self._left_diagonal(arr, i, j)

    def _right_diagonal(self, arr, i, j):
        return self._is_a_diagonal_mas(arr, i, j, [-1, 1]) or self._is_a_diagonal_mas(arr, i, j, [1, -1])

    def _left_diagonal(self, arr, i, j):
        return self._is_a_diagonal_mas(arr, i, j, [-1, -1]) or self._is_a_diagonal_mas(arr, i, j, [1, 1])


    @classmethod
    def _is_a_diagonal_mas( cls,arr, i, j, delta):
        return all( cls.reqs_to_be_a_mas(arr, i, j, delta))

    @classmethod
    def reqs_to_be_a_mas(cls, arr, i, j, delta):
            yield i - delta[0] >= 0
            yield j - delta[1] >= 0
            yield i + delta[0] >= 0
            yield j + delta[1] >= 0
            yield i - delta[0] < len(arr)
            yield j - delta[1] < len(arr[0])
            yield i + delta[0] < len(arr)
            yield j + delta[1] < len(arr[0])
            yield arr[i][j] == 'A'
            yield arr[i - delta[0]][j - delta[1]] == 'M'
            yield arr[i + delta[0]][j + delta[1]] == 'S'



stencil = FivePointStencil()

result = 0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if stencil(arr, i, j):
            result += 1


print(result)
