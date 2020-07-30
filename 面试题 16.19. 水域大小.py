def pondSizes(land: [[int]]) -> [int]:
    res = []
    m, n = len(land), len(land[0])
    def count(i: int, j: int) -> int:
        if land[i][j] == 0:
            land[i][j] = -1
            size = 1
            if i > 0:
                size += count(i-1,j)
            if i < m-1:
                size += count(i+1,j)
            if j > 0:
                size += count(i,j-1)
            if j < n-1:
                size += count(i,j+1)
            if i > 0 and j > 0:
                size += count(i-1,j-1)
            if i > 0 and j < n-1:
                size += count(i-1,j+1)
            if i < m-1 and j > 0:
                size += count(i+1,j-1)
            if i< m-1 and j < n-1:
                size += count(i+1,j+1)
            return size
        else:
            return 0
    for i in range(m):
        for j in range(n):
            if land[i][j] == 0:
                res.append(count(i,j))
    return sorted(res)