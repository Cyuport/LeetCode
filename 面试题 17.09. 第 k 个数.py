def getKthMagicNumber(k: int) -> int:
        dp, a, b, c = [1] * k, 0, 0, 0
        for i in range(1, k):
            n3, n5, n7 = dp[a] * 3, dp[b] * 5, dp[c] * 7
            dp[i] = min(n3, n5, n7)
            if dp[i] == n3:
                a += 1
            if dp[i] == n5:
                b += 1
            if dp[i] == n7:
                c += 1
        return dp[-1]

print(getKthMagicNumber(7))