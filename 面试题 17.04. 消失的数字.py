def missingNumber(nums: [int]) -> int:
    n = len(nums)
    return (1+n)*n//2 - sum(nums)