def findDuplicate(nums: [int]) -> int:
    slow, fast = nums[nums[0]], nums[nums[nums[0]]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    slow = nums[0]
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return fast
if __name__ == '__main__':
    print(findDuplicate([2,5,9,6,9,3,8,9,7,1]))