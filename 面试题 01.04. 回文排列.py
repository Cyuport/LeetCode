def canPermutePalindrome(s: str) -> bool: #位运算哈希表
    sum = 0
    for c in s:
        sum ^= 1 << ord(c)
    res = 0
    while sum:
        if sum&1 == 1:
            res += 1
            if res > 1:
                return False
        sum >>= 1
    return True

print(canPermutePalindrome("AaBb//a"))