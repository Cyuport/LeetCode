def containsDuplicate(nums: [int])->bool:
    return len(nums) == len(set(nums))


if __name__ == '__main__':
    example = [1,2,3,1]
    print(len(example))
    print(sum(set(example)))