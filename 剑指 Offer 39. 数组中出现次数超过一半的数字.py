def majorityElement(nums: [int]) -> int:
    '''nums = sorted(nums)
    return nums[len(nums)//2]'''
    vote, x = 0, nums[0] #摩尔投票
    for num in nums:
        if vote == 0:
            x = num
            vote += 1
        else:
            if num != x:
                vote -= 1
            else:
                vote += 1
    return x

print(majorityElement([1,2,2,2,3,3,3,3,3,3,4]))