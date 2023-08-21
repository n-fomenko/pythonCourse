"""
Variant 13
Perform a cyclic shift of the elements of a rectangular matrix by n elements to the right or down
(depending on the entered mode), n may be greater than the number of elements in a row or column.
"""


def cyclic_shift(matrix, n, mode):
    """
    the fact that n can be greater than the number of elements in a row or column
    is taken into account by using the % operator

    :param matrix: initial matrix as a two-dimensional list
    :param n: int, by how many elements the shift is performed
    :param mode: right or down
    :return: shifted matrix
    """
    rows = len(matrix)
    columns = (len(matrix[0]))

    matrix = [row[-n % columns:] + row[:-n % columns] if mode == 'right' else row for row in matrix]
    matrix = matrix[-n % rows:] + matrix[:-n % rows] if mode == 'down' else matrix

    return matrix


a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
shifted_a = cyclic_shift(a, 2, mode='right')
print(shifted_a)
