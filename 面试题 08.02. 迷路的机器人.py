def pathWithBostacles(obstacleGrid: [[int]]) -> [[int]]:
    r = len(obstacleGrid)
    if not r:
        return []
    c = len(obstacleGrid[0])
    res = []
    if obstacleGrid[0][0] == 1:
        return []

    def move(i: int, j: int, path: [[int]]):
        if len(res):
            return
        tmp = path + [[i, j]]
        obstacleGrid[i][j] = 1 #剪枝
        if i == r - 1 and j == c - 1:
            res.append(list(tmp))
            return
        if i < r - 1 and obstacleGrid[i + 1][j] == 0:
            move(i + 1, j, tmp)
        if j < c - 1 and obstacleGrid[i][j + 1] == 0:
            move(i, j + 1, tmp)

    move(0, 0, [])
    return res[0] if len(res) > 0 else []

print(pathWithBostacles(
[[0,0,0],[0,1,0],[0,0,0]]))