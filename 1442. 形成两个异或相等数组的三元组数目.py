def countTriplets(arr: [int]) -> int: #n^2,并不最优
    n = len(arr)
    count = 0
    for i in range(n-1):
        tmp = arr[i]
        for k in range(i+1,n):
            tmp ^= arr[k]
            if tmp == 0:
                count += (k-i)
    return count


print(countTriplets([1,1,1,1,1]))
