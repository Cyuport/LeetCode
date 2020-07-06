letter = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

def letterCombinations(digits:str)->[str]:
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return letter[ord(digits[0])-ord('2')]
    tmp = letterCombinations(digits[1:])
    ans = []
    for l in letter[ord(digits[0])-ord('2')]:
        for t in tmp:
            ans.append(l+t)
    return ans


if __name__ == '__main__':
    print(letterCombinations('23'))
