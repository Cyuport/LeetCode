def minCostClimbingStairs(cost: [int]) -> int:
    n = len(cost)
    dp = [cost[0], cost[1]]
    for i in range(2, n):
        dp.append(min(dp[i-2], dp[i-1]) + cost[i])
    return min(dp[n-1], dp[n-2])

if __name__ == '__main__':
    print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
