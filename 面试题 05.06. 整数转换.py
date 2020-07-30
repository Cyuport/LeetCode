def convertInteger(A: int, B: int) -> int:
    A,B = A&0xffffffff, B&0xffffffff
    return bin(A^B).count('1')

