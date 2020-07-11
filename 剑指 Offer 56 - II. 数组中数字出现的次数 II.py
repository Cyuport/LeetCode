def singleNumber(nums: [int]) -> int:
    cnt = {}
    for i in nums:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    for k,v in cnt.items():
        if v == 1:
            return k #哈希表，时间复杂度O(n),空间复杂度O(n)

