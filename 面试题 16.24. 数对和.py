import collections

def pairSums(nums: [int], target: int) -> [[int]]: #可用排序+双指针，这里使用哈希表
    dic = collections.defaultdict(int)
    n = len(nums)
    if n == 0:
        return []
    res = []
    for i in range(n):
        another = target-nums[i]
        if dic[another] > 0:
            res.append([another,nums[i]])
            dic[another] -= 1
        else:
            dic[nums[i]] += 1
    return res