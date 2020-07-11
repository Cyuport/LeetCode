def twoSum(n: int) -> [float]:
    dp = [[0 for _ in range(6*n)] for _ in range(n)]
    for i in range(6):
        dp[0][i] = 1

    '''def res(n: int, k: int) -> int: #n个骰子出k的情况总数
        if n == 1:
            return dp[0][k-1]
        if dp[n-1][k-1]:
            print("cache")
            return dp[n-1][k-1]
        cnt = 0
        for i in range(1,7):
            cnt += res(n-1,k-i)
        dp[n-1][k-1] = cnt
        return cnt

    for i in range(n, 6*n+1):
        res(n,i)''' #递归解法是正确的，但会超时
    for i in range(1,n): #i+1代表骰子数
        for j in range(i,6*i+6):   #j+1代表点数
            end = min(6,j)
            for k in range(end):
                dp[i][j] += dp[i-1][j-k-1]
    #可以继续优化成只使用两行数组


    total = sum(dp[n-1][n-1:])
    return [x/total for x in dp[n-1][n-1:]]

print(twoSum(2))







    