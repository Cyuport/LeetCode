def exchange(nums:[int]) -> [int]:
    odd, even = [], []
    for i in nums:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd + even

print(exchange([1,2,3,4]))