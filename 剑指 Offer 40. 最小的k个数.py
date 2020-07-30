import heapq

def getLeastNumbers(arr: [int], k: int) -> [int]: #大根堆，由于python里为小根堆所以取反
    if k == 0:
        return []

    hp = [-x for x in arr[:k]]
    heapq.heapify(hp)
    for i in range(k,len(arr)):
        if -hp[0] > arr[i]:
            heapq.heappop(hp)
            heapq.heappush(hp,-arr[i])
    ans = [-x for x in hp]
    return ans