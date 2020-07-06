def titleToNumber(s: str) -> int:
    count = 1
    ans = 0
    for i in range(len(s)-1,-1,-1):
        ans += (ord(s[i]) - 64) * count
        count *= 26
    return ans

if __name__ == '__main__':
    print(titleToNumber("ZY"))