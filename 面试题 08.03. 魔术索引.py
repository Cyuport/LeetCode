def findMagicIndex(nums: [int]) -> int:
    for i in range(len(nums)):
        if i == nums[i]:
            return i
    return -1

