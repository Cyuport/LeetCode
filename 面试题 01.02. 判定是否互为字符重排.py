import string

def CheckPermutation0(s1: str, s2: str) -> bool:
    dic1, dic2 = dict.fromkeys(string.ascii_lowercase,0), dict.fromkeys(string.ascii_lowercase,0)
    for c in s1:
        if c in dic1:
            dic1[c] += 1
        else:
            dic1[c] = 1
    for c in s2:
        if c in dic2:
            dic2[c] += 1
        else:
            dic2[c] = 1
    for ((k1,v1),(k2,v2)) in zip(dic1.items(),dic2.items()):
        if v1 != v2:
            return False
    return True

def CheckPermutation1(s1: str, s2: str) -> bool:
    sum = 0
    sum1, sum2 =0, 0
    for c in s1:
        temp = ord(c)
        sum ^= temp
        sum1 += temp
    for c in s2:
        temp = ord(c)
        sum ^= temp
        sum2 += temp
    return sum == 0 and sum1 == sum2

print(CheckPermutation1("abc","bac"))