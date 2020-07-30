def findSwapValues(array1: [int], array2: [int]) -> [int]:
    s1, s2 = sum(array1), sum(array2)
    diff = s2-s1
    if diff&1 == 1:
        return []
    array1, array2 = sorted(array1), sorted(array2)
    def findTarget(target:int) -> int: #查找有无对应元素可改为哈希，时间复杂度降为O(n)+O(n)
        i, j = 0, len(array2)-1
        while i<=j:
            m = (i+j)//2
            if array2[m] == target:
                return m
            elif array2[m] > target:
                j = m-1
            else:
                i = m+1
        return -1
    for i in array1:
        pos = findTarget(i+diff//2)
        if pos != -1:
            return [i,array2[pos]]
    return []