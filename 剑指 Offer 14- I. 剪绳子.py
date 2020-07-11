def cuttingRope(n: int) -> int:
    dp = [0]*(n+1)
    dp[1] = 1
    def helper(n: int) -> int:
        if dp[n] != 0:
            return dp[n]
        temp = 0
        for i in range(1,n):
            temp = max(temp, i*helper(n-i), i*(n-i))
        dp[n] = temp
        return dp[n]
    helper(n)
    print(dp)
    return dp[n]

print(cuttingRope(10))