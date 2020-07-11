def reverseWords(s: str) -> str:
    words = s.split()
    res = ''
    '''for i in range(len(words)-1,-1,-1):
        if res:
            res += " "
        res += words[i]
    return res'''
    return ' '.join(words)

print(reverseWords( " the  sky is blue."))


