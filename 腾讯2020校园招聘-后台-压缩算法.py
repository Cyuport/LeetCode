def myUnzip(s: str) -> str:
    i = 0
    length = len(s)
    while i < length:
        if s[i] == ']':
            j = i - 1
            while s[j] != '[':
                j -= 1
            temp = ''
            k = j + 1
            count = 0
            while ord('0')<=ord(s[k])<=ord('9'):
                count = count*10+int(s[k])
                k += 1
            for _ in range(count):
                temp += s[k+1:i]
            s = s[:j]+temp+s[i+1:]
            i = j+len(temp)-1
        i += 1
        length = len(s)
    return s


print(myUnzip('HG[3|B[2|CA]]F'))




