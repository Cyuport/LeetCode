import collections

def groupAnagrams(strs:[str]) -> [[str]]:
    if len(strs) == 0:
        return []
    dict = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - 97] += 1
        dict[tuple(count)].append(s)
    return dict.values()


if __name__ == '__main__':
    print(groupAnagrams(["",""]))
