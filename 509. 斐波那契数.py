f = [-1] * 31
f[0], f[1] = 0, 1

def fib(N: int) -> int:
    if N == 0:
        return 0
    if N == 1:
        return 1
    f0 = fib(N-2) if f[N-2] == -1 else f[N-2]
    f1 = fib(N-1) if f[N-1] == -1 else f[N-1]
    ans = f0 + f1
    f[N] = ans
    return ans


