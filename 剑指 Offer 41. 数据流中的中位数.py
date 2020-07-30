import heapq

class MedianFinder:

    def __init__(self): #A为小顶堆，保存较大的一半数，B为大顶堆，保存较小的一半数
        self.A, self.B = [], []

    def addNum(self, num: int) -> None:
        if len(self.A) == len(self.B): #需要向A插入，方法是先插入B，再把B堆顶的插入A
            heapq.heappush(self.B, -num)
            heapq.heappush(self.A, -heapq.heappop(self.B))
        else:
            heapq.heappush(self.A, num)
            heapq.heappush(self.B, -heapq.heappop(self.A))

    def findMedian(self) -> float:
        if len(self.A) == len(self.B):
            return (self.A[0] - self.B[0])/2
        else:
            return self.A[0]
