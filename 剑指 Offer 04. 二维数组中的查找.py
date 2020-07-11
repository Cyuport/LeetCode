def findNumberIn2DArray(matrix: [[int]], target: int) -> bool:
    n = len(matrix)
    if n == 0:
        return False
    m = len(matrix[0])
    i, j = n-1, 0
    while i >= 0 and j < m:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            j += 1
        else:
            i -= 1
    return False

print(findNumberIn2DArray([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],20))

