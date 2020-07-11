def firstUniqChar(s: str) -> str:
    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    for k,v in dic.items():
        if v == 1:
            return k
    return ' '