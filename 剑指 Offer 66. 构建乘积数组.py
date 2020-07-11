def constructArr(a: [int]) -> [int]:
    if not len(a):
        return []
    l, r = [1], [1]
    for i in range(1, len(a)):
        l.append(l[-1]*a[i-1])
        r.append(r[-1]*a[-i])
    res = [r[-1]]
    for i in range(1,len(a)-1):
        res.append(l[i]*r[-1-i])
    res.append(l[-1])
    return res

print(constructArr([1,2,3,4,5]))