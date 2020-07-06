def heightChecker(heights: [int]) -> int:
    count = [0] * 100
    for h in heights:
        count[h - 1] += 1
    target = []
    for i in range(100):
        target += [i+1]*count[i]
    res = 0
    for i in range(len(target)):
        if target[i] != heights[i]:
            res += 1
    return res



heightChecker([1,1,4,2,1,3])

