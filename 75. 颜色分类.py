def sortColors(nums: [int]) -> None:
    n = len(nums)
    curr, p0, p2 = 0, 0, n - 1
    while curr <= p2:
        if nums[curr] == 0:
            nums[p0], nums[curr] = nums[curr], nums[p0]
            p0 += 1
            curr += 1
        elif nums[curr] == 2:
            nums[p2], nums[curr] = nums[curr], nums[p2]
            p2 -= 1
        else:
            curr += 1


if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    sortColors(nums)
    print(nums)