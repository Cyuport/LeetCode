def firstUniqChar(s: str)->int:
    dic = {c: s.count(c) for c in set(s)}
    for i,c in enumerate(s):
        if dic[c] == 1:
            return i
    return -1
