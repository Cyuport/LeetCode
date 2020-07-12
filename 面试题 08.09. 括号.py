def generateParenthesis(n: int) -> [str]:
    res = []
    def get_res(state, nl, nr): #nl,nr为左右括号分别的剩余个数
        if nl > nr:
            return
        elif len(state) == 2*n:
            res.append(state)
        if nl > 0:
            get_res(state+'(',nl-1,nr)
        if nr > 0:
            get_res(state+')',nl,nr-1)
    get_res('',n,n)
    return res

print(generateParenthesis(3))