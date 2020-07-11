def isStraight(nums: [int]) -> bool:
    count = 0
    mi, ma = 13, 1
    for i in nums:
        if i == 0:
            count += 1
        else:
            if i < mi:
                mi = i
            if i > ma:
                ma = i
    if count == 0:
        return ma - mi == 4 and len(set(nums)) == 5
    return ma - mi <= 4 and len(set(nums)) - 1 == 5 - count


print(isStraight([9,4,2,5,6]))
