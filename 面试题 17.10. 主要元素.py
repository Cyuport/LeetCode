def majorityElement(nums: [int]) -> int:
    #摩尔投票算法，本质是每次丢弃一对不同数字，则如果有主元素，则主元素最后必定会剩下
    n, count = nums[0], 1
    for i in nums[1:]:
        if count == 0:
            n = i
            count = 1
        elif i == n:
            count += 1
        else:
            count -= 1
    count  = 0
    for i in nums:
        if i == n:
            count += 1
    if count > len(nums)//2:
        return n
    else:
        return -1

print(majorityElement([3,3,4]))