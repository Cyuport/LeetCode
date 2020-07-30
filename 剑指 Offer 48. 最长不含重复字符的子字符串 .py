def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0
    dic = {}
    dp = [0] * len(s)
    dp[0] = 1
    dic[s[0]] = 0
    for j in range(1,len(s)):
        i = dic.get(s[j],-1)
        dic[s[j]] = j
        if dp[j-1] >= j-i:
            dp[j] = j-i
        else:
            dp[j] = dp[j-1]+1
    return max(dp)


print(lengthOfLongestSubstring("abcabcbb"))