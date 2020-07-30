def exchange(nums:[int]) -> [int]:
    odd, even = [], []
    for i in nums:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd + even

def exchange2(nums:[int]) -> [int]: #双指针法
    i, j = 0, len(nums) - 1
    while i < j:
        while i < j and nums[i] & 1 == 1:
            i += 1
        while i < j and nums[j] & 1 == 0:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    return nums


print(exchange([1,2,3,4]))