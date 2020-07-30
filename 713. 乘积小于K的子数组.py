def numSubarrayProductLessThanK(nums: [int], k: int) -> int:
    #双指针法，每次将right端右移一位，并右移left直到满足条件，则以right位置结尾的满足条件的子数组有right-left+1个
    if k <= 1:
        return 0
    count = 0
    i, j = 0, 0
    count, tmp = 0, 1
    for j in range(len(nums)):
        tmp *= nums[j]
        while tmp >= k:
            tmp /= nums[i]
            i += 1
        print("i={},j={}".format(i,j))
        count += j - i + 1
    return count


print(numSubarrayProductLessThanK([10,5,2,6],100))