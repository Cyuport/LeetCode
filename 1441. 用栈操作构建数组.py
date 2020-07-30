def buildArray(target: [int], n: int) -> [str]:
    res = []
    j = 1
    for i in range(len(target)):
        while target[i] != j:
            res.append('Push')
            res.append('Pop')
            j += 1
        res.append('Push')
        j += 1
    return res


print(buildArray([2,3,4],4))
