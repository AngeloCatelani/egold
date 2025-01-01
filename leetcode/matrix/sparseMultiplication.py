# 311. Sparse Matrix Multiplication
# Given two sparse matrices A and B, return the result of AB.

# You may assume that A's column number is equal to B's row number.

# Example:

# Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

# Output:

#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |
# Difficulty:
# Medium


def multiply( mat1, mat2) :
    m = len(mat1)
    n = len(mat2)
    l = len(mat2[0])

    ans = [[0]*l for _ in range(m)] #[[0, 0, 0], [0, 0, 0]] length of m.When you are not interested in some values returned by a function we use underscore in place of variable name . Basically it means you are not interested in how many times the loop is run till now just that it should run some specific number of times overall.
    for i in range(m):
        for j in range(n):
            for k in range(l):
                ans[i][j] += mat1[i][k] * mat2[k][j]
    return ans

    # Time: O(mnl)
# Space: O(nl)

print(multiply(A,B))