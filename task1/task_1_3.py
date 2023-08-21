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

    if mode == 'right':
        for i in range(rows):
            matrix[i] = matrix[i][-n % columns:] + matrix[i][:-n % columns]
    elif mode == 'down':
        matrix = matrix[-n % rows:] + matrix[:-n % rows]

    return matrix
