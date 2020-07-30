def threeSum(nums: [int]) -> [[int]]:
    nums = sorted(nums)
    res = []
    for a in range(len(nums)):
        if a > 0 and nums[a] == nums[a-1]:
            continue
        b, c = a + 1, len(nums) - 1
        while b < c:
            if nums[b]+nums[c]<-nums[a]:
                b += 1
            elif nums[b]+nums[c]>-nums[a]:
                c -= 1
            else:
                res.append([nums[a],nums[b],nums[c]])
                tb, tc = nums[b], nums[c]
                while b < c and nums[b] == tb:
                    b += 1
                while b < c and nums[c] == tc:
                    c -= 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))