def majorityElement(nums: [int]) -> int:
    nums = sorted(nums)
    return nums[len(nums)//2]