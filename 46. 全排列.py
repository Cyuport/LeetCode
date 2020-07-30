def permute(nums: [int]) -> [[int]]:
    res = []
    def help(x: int):
        if x == len(nums)-1:
            res.append(list(nums))
            return
        for i in range(x,len(nums)):
            nums[x], nums[i] = nums[i], nums[x]
            help(x+1)
            nums[x], nums[i] = nums[i], nums[x]

    help(0)
    return res


print(permute([1,2,3]))