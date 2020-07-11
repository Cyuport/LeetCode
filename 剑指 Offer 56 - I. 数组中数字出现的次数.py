def singleNumbers(nums: [int]) -> [int]:
    a = 0
    for i in nums:
        a ^= i
    mask = 1
    for i in range(32):
        if a & mask:
            break
        mask <<= 1
    b = 0
    for i in nums:
        if i & mask:
            b ^= i
    return (a^b, b)

print(singleNumbers([1,2,4,1,4,6]))