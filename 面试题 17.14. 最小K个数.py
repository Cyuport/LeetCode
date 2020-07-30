import heapq

def smallestK(arr: [int], k: int) -> [int]:
    if len(arr) == 0 or k == 0:
        return []
    hq = [-i for i in arr[:k]]
    heapq.heapify(hq)
    for a in arr[k:]:
        if -a > hq[0]:
            heapq.heappop(hq)
            heapq.heappush(hq,-a)
    res = [-i for i in hq]
    return res
