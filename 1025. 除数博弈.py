def divisorGame(N: int) -> bool:
    if N <= 1:
        return False
    dp = [0 for i in range(N+1)]
    dp[2] = 1
    for i in range(3,N+1):
        for j in range(1,int(i**0.5)):
            if i%j == 0 and dp[i-j] == 0:
                dp[i] = 1
    return dp[N] == 1


if __name__ == '__main__':
    print(divisorGame(3))