def findDisappearedNumbers(nums: [int]) -> [int]:
    n = len(nums)
    res = []
    for i in range(n):
        nums[nums[i] % n - 1] += n
    for i in range(n):
        if nums[i] <= n:
            res.append(i + 1)
    return res

def findDisappearedNumbers1(nums: [int]) -> [int]:
    n = len(nums)
    res = []
    for i in range(n):
        while nums[i] != nums[nums[i] - 1]:
            a, b = i, nums[i] - 1
            nums[a], nums[b] = nums[b], nums[a]
    return [i + 1 for i in range(n) if nums[i] != i + 1]


def test(nums: [int]) -> [int]:

    def swap(nums, i1, i2):
        if i1 == i2:
            return
        nums[i1] = nums[i1] ^ nums[i2]
        nums[i2] = nums[i1] ^ nums[i2]
        nums[i1] = nums[i1] ^ nums[i2]

    l = len(nums)
    for i in range(l):
        while (nums[i] != nums[nums[i] - 1]):  # 每次交换至少将一个鸽子放到正确的位置，直到当前巢有正确的鸽子
            swap(nums, i, nums[i] - 1)

    return [i + 1 for i in range(l) if nums[i] != (i + 1)]


if __name__ == '__main__':
    print(test([4,3,2,7,8,2,3,1]))
    print(findDisappearedNumbers1([4,3,2,7,8,2,3,1]))