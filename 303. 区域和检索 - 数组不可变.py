class NumArray:
    def __init__(self, nums: [int]):
        self.array = [0]
        for i in range(len(nums)):
            self.array.append(self.array[i]+nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.array[j+1] - self.array[i]


if __name__ == '__main__':
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print(obj.array)
    p1 = obj.sumRange(0,5)
    print(p1)