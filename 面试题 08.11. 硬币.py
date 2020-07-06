def waysToChange(n: int) -> int:
    if n == 0:
        return 0
    dp = [1]
    for i in range(1,5):
        dp.append(dp[i-1])
    for i in range(5,10):
        dp.append(dp[i-1]+dp[i-5])
    for i in range(10,25):
        dp.append(dp[i-1]+dp[i-5]+dp[i-10])
    dp.append(1 + dp[24] + dp[20] + dp[15])
    print("dp=",dp[1:])
    if n <= 25:
        return dp[n]
    for i in range(26,n+1):
        dp.append(dp[i-1]+dp[i-5]+dp[i-10]+dp[i-25])
    return dp[n]


if __name__ == '__main__':
    print(waysToChange(10))

