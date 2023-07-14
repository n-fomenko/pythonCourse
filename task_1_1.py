"""
Option 11
The coefficients of a system of linear equations are given as a rectangular matrix.
With the help of permissible transformations to bring the system to a triangular form.
Find the number of rows whose arithmetic mean is less than the given value.
"""

a = [[2, 5, 2, -38], [3, -2, 4, 17], [-6, 1, -7, -12]]
column = len(a[0])
for i in range(len(a)):
    for kj in range(i):
        a[i] = [a[kj][j] * a[i][kj] - a[i][j] for j in range(column)]
    a[i] = [element / a[i][i] for element in a[i]]

print()
print(*a, sep='\n')

a1 = [[2, 5, 2, -38], [3, -2, 4, 4, 17], [-6, 1, -7, -12]]
check_mean = 5
counter = 0

x = sum(sum(i)/len(i) < check_mean for i in a1)
print(x)
# for i in range(3):
#     mean_r = sum(a1[i])
#     if mean_r < check_mean:
#         counter += 1
#     print(mean_r)
# print(counter)



for i in range(len(a[0])):
    a[0] = [element / a[0][0] for element in a[0]]

    a[i + 1] = [a[0][j] * a[1][0] - a[1][j] for j in range(column)]

    a[1] = [element / a[1][1] for element in a[1]]

    a[i + 2] = [a[0][j] * a[2][0] - a[2][j] for j in range(column)]
    a[i + 2] = [a[1][j] * a[2][1] - a[2][j] for j in range(column)]

    a[2] = [element / a[2][2] for element in a[2]]
    break
print()
print()

print(*a, sep='\n')

# Scale the 1st row so that its first nonzero entry is equal to 1.

# for i in range(len(a[0])):
#     # if a[0][0] != 0:
#     a[0][i] /= n

# Use row replacement so all entries below this 1 are 0.
# for i in range(2):
#     diff = []
#     for j in range(len(a[0])):
#         diff.append(a[0][j] * a[i + 1][0] - a[i + 1][j])
#     a[i + 1] = diff


# n = a[1][1]
# for i in range(len(a[1])):
#     # if a[0][0] != 0:
#     a[1][i] /= n


# for i in range(0):
#     diff = []
#     for j in range(len(a[0])):
#         diff.append(a[i + 2][j] - a[1][j] * a[i + 2][1] / a[1][1])
#     a[i + 2] = diff
# print()

# print(*a, sep='\n')
#
#
#
# diff = []
# for j in range(len(a[0])):
#     diff.append(a[2][j] - a[1][j] * a[2][1])
# a[2] = diff
#
# n = a[2][2]
# for i in range(len(a[2])):
#     # if a[0][0] != 0:
#     a[2][i] /= n
# #
# print()
# print(*a, sep='\n')
#
# for i in range(1):
#     diff = []
#     for j in range(len(a[0])):
#         diff.append(a[i + 2][j] - a[1][j] * a[i + 2][2] / a[1][2])
#     a[i + 2] = diff
# print()
# print(*a, sep='\n')
# if a[1][0] < a[0][0] and a[1][0] < a[2][0]:
