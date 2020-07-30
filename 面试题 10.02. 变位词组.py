import collections


def groupAnagrams(strs:[str]) -> [[str]]:
    #排序+哈希
    dic = collections.defaultdict(list)
    for word in strs:
        tmp = ''.join(sorted(word))
        dic[tmp].append(word)
    res = []
    for k,v in dic.items():
        res.append(v)
    return res
