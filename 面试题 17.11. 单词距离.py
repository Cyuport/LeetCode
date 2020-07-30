import collections


def findClosest(words:[str], word1:str, word2:str) -> int:
    pos = collections.defaultdict(list)
    for i in range(len(words)):
        pos[words[i]].append(i)
    a, b = pos[word1], pos[word2]
    i, j = 0, 0
    tmp = 0x7fffffff
    while i < len(a) and j < len(b):
        if a[i]<b[j]:
            tmp = min(tmp,b[j]-a[i])
            i += 1
        else:
            tmp = min(tmp,a[i]-b[j])
            j += 1
    return tmp