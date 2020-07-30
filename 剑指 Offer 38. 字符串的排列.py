def permutation(s: str) -> [str]:
    res = []
    if len(s) == 1:
        return [s[0]]
    for i in range(len(s)):
        l,r = s[:i], s[i+1:]
        tmp = permutation(l + r)
        tmp = [s[i]+_ for _ in tmp]
        res += tmp
    return list(set(res))


print(permutation("aab"))

def permutation2(s:str) -> [str]:
    c, res = list(s), []
    def dfs(x: int):
        if x == len(c) - 1:
            res.append(''.join(c))
            return
        dic = set()
        for i in range(x,len(c)):
            if c[i] in dic:
                continue
            dic.add(c[i])
            c[x], c[i] = c[i], c[x]
            dfs(x+1)
            c[x], c[i] = c[i], c[x]
    dfs(0)
    return res

print(permutation2("aab"))