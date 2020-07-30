def getValidT9Words(num: str, words: [str]) -> [str]:
    alphaToNum = ['2','2','2','3','3','3','4','4','4','5','5','5','6','6','6','7','7','7','7','8','8','8','9','9','9','9']
    res = []
    n = len(num)
    for word in words:
        if len(word) != n:
            continue
        tmp = ''
        for c in word:
            tmp += alphaToNum[ord(c)-ord('a')]
        if num == tmp:
            res.append(word)
    return res