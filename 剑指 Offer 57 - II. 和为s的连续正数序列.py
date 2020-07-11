def findContinuousSequence(target: int) -> [[int]]:
    left, right = 1, 2
    res = []
    temp_sum = 3
    for left in range(1, target//2 + 1):
        while temp_sum < target:
            right += 1
            temp_sum += right
        if temp_sum == target:
            res.append([x for x in range(left,right+1)])
        right = left + 2
        temp_sum = left + right + 1
    return res

