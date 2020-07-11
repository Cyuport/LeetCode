def maxValue(grid: [[int]]) -> int:
    m, n = len(grid), len(grid[0])
    value = [[0 for i in range(n)] for j in range(m)]
    value[0][0] = grid[0][0]
    for i in range(1,n):
        value[0][i] = value[0][i-1] + grid[0][i]
    for i in range(1,m):
        value[i][0] = value[i-1][0] + grid[i][0]
    for i in range(1,m):
        for j in range(1,n):
            value[i][j] = max(value[i-1][j], value[i][j-1]) + grid[i][j]
    print(value)
    return value[m-1][n-1]


print(maxValue([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))


