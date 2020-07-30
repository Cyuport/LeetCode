def subsets(nums:[int]) -> [[int]]:
    res = []
    n = len(nums)

    def helper(i:int,tmp:[int]):
        res.append(tmp)
        for j in range(i,n):
            helper(j+1,tmp+[nums[j]])

    helper(0,[])
    return res