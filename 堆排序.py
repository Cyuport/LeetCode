#堆通常用一维数组实现，父节点i的左子节点在2i+1,右子节点在2i+2；子节点i的父节点在(i-1)//2
def heapSort(lst): #最大堆
    def heapify(start,end): #调整从start到end的最大堆
        root = start
        while True:
            child = 2 * root + 1
            if child > end: #没有子节点了，root已经是叶节点，结束调整
                break
            if child + 1 <= end and lst[child] < lst[child+1]:
                child += 1 #当父节点较小时，和较大的那个子节点交换，保证交换后的父节点是三个节点中最大的
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child #继续向下调整刚刚交换下去的原父节点
            else: #父节点已最大，不需继续调整
                break

    #建立最大堆，建堆的时间复杂度是O(n),可以把建堆过程想成先对左子树建堆(T(n/2))，再对右子树建堆(T(n/2))，最后对根下溯(O(lg n))，所以递推式是
    #T(n) = 2*T(n/2) + O(lg n)
    for start in range((len(lst)-2)//2,-1,-1):
        heapify(start,len(lst)-1)

    #堆排序
    for end in range(len(lst)-1,0,-1):
        lst[0],lst[end]=lst[end],lst[0] #最大元素现在位于end
        heapify(0,end-1)
    return lst



print(heapSort([1,3,5,7,9,2,4,6,8,0]))
