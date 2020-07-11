def permutation(S: str) -> [str]:
    ans = []
    def back(cur,res):
        if not cur:
            ans.append(res)
        for i in range(len(cur)):
            back(cur[:i]+cur[i+1:],res+cur[i])
    back(S,'')
    return ans


print(permutation("abc"))
