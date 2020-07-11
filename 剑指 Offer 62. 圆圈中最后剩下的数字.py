def lastRemaining(n: int, m: int) -> int:
    nums = [x for x in range(n)]
    pos = -1
    while len(nums)>1:
        pos += m
        pos %= len(nums)
        del nums[pos]
        pos -= 1
    return nums[0]


print(lastRemaining(10,17))