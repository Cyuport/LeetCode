def isSubsequence(s: str, t: str) -> bool:
    ls, lt = len(s), len(t)
    if ls == 0:
        return True
    if ls > lt:
        return False
    dp = [[0 for j in range(lt)] for i in range(ls)] #dp[i][j]表示s[i]是否是t[j]的子序列
    if s[0] == t[0]:
        dp[0][0] = 1
    for j in range(1,lt):
        if dp[0][j-1] == 1 or s[0] == t[j]:
            dp[0][j] = 1
    for i in range(1,ls):
        for j in range(1,lt):
            if s[i] == t[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[ls-1][lt-1] == 1

if __name__ == '__main__':
    s = "axc"
    t = "ahbgdc"
    print(isSubsequence(s,t))

