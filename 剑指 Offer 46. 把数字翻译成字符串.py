def translateNum(num: int) -> int:
    s = str(num)
    i = 0
    count = 0
    if len(s) == 1:
        return 1

    def helper(i: int):
        nonlocal count
        if i == len(s)-1:
            count += 1
            return
        if s[i] == '0' or s[i] > '2':
            helper(i+1)
        elif s[i] == '1':
            helper(i+1)
            if i+2<len(s):
                helper(i+2)
        elif s[i] == '2':
            helper(i+1)
            if i+1<len(s) and '0' <= s[i+1] <= '5':
                helper(i+2)

    helper(0)
    return count


def translateNum2(num: int) -> int:
    if num == 0:
        return 1
    elif num %100 > 25 or num%100>=0 and num%100<=9:
        return translateNum(num//10)
    elif 10 <= num%100 <=25:
        return translateNum(num//100)+translateNum(num//10)

print(translateNum(25))






