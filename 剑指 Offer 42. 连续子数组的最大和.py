def maxSubArray(nums: [int]) -> int:
    dp = [nums[0]]
    temp = dp[0]
    for i in range(1, len(nums)):
        dp.append(max(dp[i-1]+nums[i], nums[i]))
        if dp[i] > temp:
            temp = dp[i]
    return temp


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))