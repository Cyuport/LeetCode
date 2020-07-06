def productExceptSelf(nums:[int])->[int]:
    pre = [nums[0]]
    suff = [nums[-1]]
    for i in range(1, len(nums)):
        pre.append(pre[-1]*nums[i])
        suff.append(suff[-1]*nums[-1-i])
    ans = [suff[-2]]
    for i in range(1,len(nums)-1):
        ans.append(pre[i-1]*suff[-2-i])
    ans.append(pre[-2])
    return ans


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(productExceptSelf(nums))
