def missingTwo(nums: [int]) -> [int]:
    N = len(nums)+2
    sum1 = (1+N)*N//2 - sum(nums)
    sum2 = 0
    for i in range(1,N+1):
        sum2 += i**2
    for i in nums:
        sum2 -= i**2
    product = (sum1**2-sum2)//2
    delta = (sum1**2-4*product)**0.5
    return [(sum1+delta)//2,(sum1-delta)//2]
