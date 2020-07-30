def subsets(nums: [int]) -> [[int]]:
    res = [[]]
    for n in nums:
        res += [_+[n] for _ in res]
    return res

