def movingCount(m: int, n: int, k: int) -> int:
    visited = [([0] * n) for i in range(m)]

    def judge(i: int, j: int) -> bool:
        tmp = 0
        while i:
            tmp += i%10
            i //= 10
        while j:
            tmp += j%10
            j //= 10
        if tmp <= k:
            return True
        else:
            return False

    def move(i: int, j: int):
        nonlocal visited
        visited[i][j] = 1
        if i-1>=0 and visited[i-1][j] == 0 and judge(i-1,j):
            move(i-1,j)
        if i+1<m and visited[i+1][j] == 0 and judge(i+1,j):
            move(i+1,j)
        if j-1>=0 and visited[i][j-1] == 0 and judge(i,j-1):
            move(i,j-1)
        if j+1<n and visited[i][j+1] == 0 and judge(i,j+1):
            move(i,j+1)

    move(0,0)
    count = 0
    for i in range(m):
        for j in range(n):
            count += visited[i][j]
    return count


print(movingCount(3,1,0))
