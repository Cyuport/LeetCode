def mergeSort(arr):
    if len(arr)<2:
        return arr
    mid = len(arr)//2
    left, right = arr[:mid], arr[mid:]
    return merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    res = []
    p, q = 0, 0
    while p<len(left) and q<len(right):
        if left[p]<right[q]:
            res.append(left[p])
            p += 1
        else:
            res.append(right[q])
            q += 1
    while p<len(left):
        res.append(left[p])
        p += 1
    while q<len(right):
        res.append(right[q])
        q += 1
    return res

print(mergeSort([1,3,5,7,9,2,4,6,8,0]))