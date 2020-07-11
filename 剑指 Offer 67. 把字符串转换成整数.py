def strToInt(str: str) -> int:
    str = str.strip()
    if not str:
        return 0
    int_max, int_min = 2**31 - 1, -2**31
    res, sign = 0, 1
    if str[0] == '-':
        sign = -1
        str = str[1:]
    elif str[0] == '+':
        str = str[1:]
    for c in str:
        if not '0' <= c <= '9':
            break
        res = 10*res + ord(c)-ord('0')
    if sign > 0:
        return min(int_max,res)
    else:
        return max(int_min,-res)