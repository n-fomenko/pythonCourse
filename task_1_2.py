"""
Variant 20
An integer rectangular matrix is given. Determine:
1) the number of negative elements in those rows that contain at least one zero element;
2) row and column numbers of all saddle points of the matrix.
Note. A matrix A has a saddle point Aij if Aij is the minimum element in the i-th row and the maximum in the j-th column
"""

# Part1
a = [[1, 2, 3, 4, 10], [5, -6, 7, 8, 1], [11, 12, 13, 14, 15], [-1, -2, 0, 0, -5]]

counter = [f'row {idx} contains {sum(x < 0 for x in row)} negative elements'
           for idx, row in enumerate(a) if 0 in row]
print('\n'.join(counter))

# Part2
a1 = [[1, 2, 3, 0], [4, 5, 6, 25], [7, 8, 9, 40]]

rows = len(a1)
columns = len(a1[0])
saddle_points = [f'The saddle point has an index is {i, j} and a value: {a1[i][j]}'
                 for i in range(rows)
                 for j in range(columns)
                 if min(a1[i]) == a1[i][j] and max(col[j] for col in a1) == a1[i][j]]
print('\n'.join(saddle_points))
