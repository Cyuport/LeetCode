def findTargetSumWays(nums: [int], S: int) -> int:
    P = S + sum(nums)
    if P % 2 or S > sum(nums):
        return 0
    P //= 2
    #转变为01背包问题
    dp = [1] + [0 for _ in range(P)]
    for num in nums:
        for j in range(P, num-1, -1):
            dp[j] += dp[j - num]
    return dp[P]


if __name__ == '__main__':
    print(findTargetSumWays([1, 1, 1, 1, 1],3))