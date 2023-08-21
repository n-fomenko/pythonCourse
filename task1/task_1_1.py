"""
Variant 11
The coefficients of a system of linear equations are given as a rectangular matrix.
With the help of permissible transformations to bring the system to a triangular form.
Find the number of rows whose arithmetic mean is less than the given value.
"""
CHECK_MEAN = 5

a = [[2, 5, 2, -38], [3, -2, 4, 17], [-6, 1, -7, -12]]
column = len(a[0])

for i in range(len(a)):
    for kj in range(i):
        a[i] = [a[kj][j] * a[i][kj] - a[i][j] for j in range(column)]
    a[i] = [element / a[i][i] for element in a[i]]
print(*a, sep='\n')

# ---------Part2------------------------------
a1 = [[2, 5, 2, -38], [3, -2, 4, 4, 17], [-6, 1, -7, -12]]

counter = sum(sum(i) / len(i) < CHECK_MEAN for i in a1)
print(counter)
