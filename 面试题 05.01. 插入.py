def insertBits(N: int, M: int, i:int, j:int) -> int:
    M <<= i
    mask = 1
    for _ in range(j-i):
        mask <<= 1
        mask |= 1
    mask <<= i
    return (N & (mask^0xffffffff)) | M

print(insertBits(1143207437,1017033,11,31))

