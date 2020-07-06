def partition(s: str) -> [[str]]:
    if not s:
        return [[]]
    if len(s) == 1:
        return [[s]]
    ans = []
    for i in range(1, len(s) + 1):
        if s[:i][::-1] == s[:i]:
            ans += [[s[:i]] + j for j in partition(s[i:])]
    return ans


if __name__ == '__main__':
    print(partition("aab"))