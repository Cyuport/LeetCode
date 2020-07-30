def replaceSpaces(S: str, length: int) -> str:
    res = ''
    for i in range(length):
        if S[i] != ' ':
            res += S[i]
        else:
            res += '%20'
    return res


print(replaceSpaces("     ",5))