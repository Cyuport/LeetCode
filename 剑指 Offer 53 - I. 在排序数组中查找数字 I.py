def search(nums: [int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l+r)//2
        if nums[m] <= target:
            l = m + 1
        else:
            r = m - 1
    end = l
    if r >= 0 and nums[r] != target:
        return 0
    l = 0
    while l <= r:
        m = (l+r)//2
        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1
    begin = r
    return end - begin + 1

