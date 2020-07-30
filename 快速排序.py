def quickSort(arr: [int],left: int,right: int) -> [int]:
    if left<right:
        partitionIndex = partition(arr,left,right)
        quickSort(arr,left,partitionIndex-1)
        quickSort(arr,partitionIndex+1,right)
    return arr

def partition(arr,left,right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
        i += 1
    #结束后，index-1位置的值小于pivot，index及以后位置的值大于pivot,故把pivot交换到index-1位置
    arr[pivot],arr[index-1] = arr[index-1], arr[pivot]
    return index - 1



print(quickSort([1,3,5,7,9,2,4,6,8,0],0,9))
