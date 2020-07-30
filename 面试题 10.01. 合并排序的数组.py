def merge(A:[int], m:int, B:[int], n:int)-> None:
    a, b, i = m-1, n-1, m+n-1
    while a>=0 and b>=0:
        if A[a]>B[b]:
            A[i]=A[a]
            a -= 1
        else:
            A[i]=B[b]
            b -= 1
        i -= 1
    while b >= 0:
        A[i] = B[b]
        i -= 1
        b -= 1

