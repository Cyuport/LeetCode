def multiply(A: int, B: int) -> int:
    if A == 1:
        return B
    if B == 1:
        return A
    if A&1 == 0:
        tmp = multiply(A>>1,B)
        return tmp + tmp
    else:
        tmp = multiply(A>>1,B)
        return tmp + tmp + B