def findRepeatNumber(nums: [int]) -> int:
    cnt = {}
    for i in nums:
        if i in cnt.keys():
            return i
        cnt[i] = 1

print(findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))