def twoSum(nums: [int], target: int) -> [int]: #nlogn
    for i in nums:
        j = target - i
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2
            if nums[mid] == j:
                return [i, j]
            elif nums[mid] < j:
                if begin != mid:
                    begin = mid
                else:
                    begin += 1
            else:
                if end != mid:
                    end = mid
                else:
                    end -= 1

def twoSum2(nums: [int], target: int) -> [int]:
    i, j = 0, len(nums)-1
    temp = nums[i] + nums[j]
    while temp != target:
        if temp < target:
            i += 1
        else:
            j -= 1
        temp = nums[i] + nums[j]
    return [nums[i],nums[j]]

print(twoSum2([45,46,67,73,74,74,77,83,89,98], 147))
