def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    if n == 1:
        return x
    if n == -1:
        return 1/x
    half, rest = myPow(x, n // 2), myPow(x, n%2)
    return half*half*rest


if __name__ == '__main__':
    print(myPow(2.10000, 3))