def compressString(S: str) -> str:
    if len(S) == 0:
        return ''
    res = ''
    tmp = 1
    for i in range(1,len(S)):
        if S[i] == S[i-1]:
            tmp += 1
        else:
            res += S[i-1]
            res += str(tmp)
            tmp = 1
    res += S[-1]
    res += str(tmp)
    if len(res)>=len(S):
        return S
    return res
