def reverseBits(num: int) -> int:
    if num == 0:
        return 1
    n = str(bin(num))[2:]
    print(n)
    lens = []
    tmp = 1
    gaps = []
    gap = 0
    for i in range(1,len(n)):
        if n[i] == '0' and n[i-1] == '1':
            lens.append(tmp)
            tmp = 0
            gap = 1
        elif n[i] == '0' and n[i-1] == '0':
            gap += 1
        elif n[i] == '1' and n[i-1] == '0':
            gaps.append(gap)
            gap = 0
            tmp = 1
        else:
            tmp += 1
    if tmp:
        lens.append(tmp)
    print(lens)
    print(gaps)
    res = lens[0]+1
    for i in range(len(gaps)):
        if gaps[i] == 1:
            res = max(res,lens[i]+lens[i+1]+1)
        else:
            res = max(res,lens[i+1]+1)
    return res

print(reverseBits(45725232))

