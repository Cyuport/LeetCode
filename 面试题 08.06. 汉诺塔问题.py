def hanota(A:[int], B: [int], C: [int]) -> None:
    if len(A)<=0:
        return
    hanota(A[1:len(A)-1],C,B)
    C.append(A[-1])
    A.pop()
    hanota(B,A,C)


def help(n, A:[int], B: [int], C: [int]) -> None:
    if n <= 0:
        return
    help(n-1,A,C,B)
    C.append(A[-1])
    A.pop()
    help(n-1,B,A,C)

if __name__ == '__main__':
    s=[1,2,3]
    print(s[:len(s)-1])