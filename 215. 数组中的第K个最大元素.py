import heapq

def findKthLargest(nums: [int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


def method2(nums: [int], k: int) -> int:
    """使用小顶堆"""
    q = []
    for c in nums:
        heapq.heappush(q, c)
        while len(q) > k:
            heapq.heappop(q)
    print("1: ",q[0])
    print("2: ",heapq.heappop(q))
    return heapq.heappop(q)

if __name__ == '__main__':
    print(findKthLargest([1,3,2,3,1],3))
    method2([3,2,1,5,6,4],2)