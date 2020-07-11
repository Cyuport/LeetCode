import collections

def maxSlidingWindow(nums: [int], k: int) -> [int]:
    deque = collections.deque()
    n = len(nums)
    res = []
    for i, j in zip(range(1-k, 1+n-k), range(n)):
        if i > 0 and deque[0] == nums[i-1]:
            deque.popleft()
        while deque and nums[j] > deque[-1]:
            deque.pop()
        deque.append(nums[j])
        if i >= 0:
            res.append(deque[0])
    return res

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))