def search(nums: [int], target: int) -> int:
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return 0 if nums[0] == target else -1
    mid = len(nums)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return search(nums[:mid],target)
    else:
        tmp = search(nums[mid+1:],target)
        return mid + 1 + tmp if tmp!=-1 else -1
