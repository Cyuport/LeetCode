import heapq

def findKthLargest(nums: [int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    print(findKthLargest([1,3,2,3,1],3))