def arrangeCoins(n:int)->int:
    return floor(2**0.5 * (n+0.125)**0.5 -0.5)