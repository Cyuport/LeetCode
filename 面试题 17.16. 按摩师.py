def massage(nums:[int]) -> int:
    if len(nums) == 0:
        return 0
    dp = [[0,nums[0]]]
    for i in range(1, len(nums)):
        dp.append([max(dp[i-1]), dp[i-1][0]+nums[i]])
    return max(dp[len(dp)-1])

if __name__ == '__main__':
    print(massage([2,7,9,3,1]))
