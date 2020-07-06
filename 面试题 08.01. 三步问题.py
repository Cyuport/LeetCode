def waysToStep(n: int) -> int:
    dp = [1, 2, 4]
    for i in range(3,n):
        dp.append((dp[i-1] + dp[i-2] + dp[i-3])%1000000007)
    return dp[n-1]

if __name__ == '__main__':
    print(waysToStep(1))