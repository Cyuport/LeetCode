def numSquares(n: int) -> int:
    dp = [0]
    for i in range(1, n + 1):
        dp.append(i)
        for j in range(1, int(i ** 0.5) + 1):
            dp[i] = min(dp[i], dp[i - j**2] + 1)
    return dp[n]

if __name__ == '__main__':
    print(numSquares(13))