def minNumber(nums:[int]) -> str: ##变种的排序题
    strs = [str(num) for num in nums]
    def quickSort(l,r):
        if l<r:
            partitionIndex = partition(l,r)
            quickSort(l,partitionIndex-1)
            quickSort(partitionIndex+1,r)
        return

    def partition(l,r):
        pivot = l
        index = pivot+1
        i = index
        print("index=",index)
        while i<=r:
            if strs[i]+strs[pivot]<strs[pivot]+strs[i]:
                strs[i],strs[index] = strs[index],strs[i]
                index += 1
            i += 1
        strs[pivot],strs[index-1]=strs[index-1],strs[pivot]
        return index-1
    quickSort(0,len(strs)-1)
    return ''.join(strs)

print(minNumber([3,30,34,5,9]))