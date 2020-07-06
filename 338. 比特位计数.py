def countBits(nums: int) -> [int]:
    res = [0]
    tmp = []
    count = 0
    n = nums
    while n > 0:
        count += 1
        n >>= 1
    for i in range(count):
        for j in range(len(res)):
            tmp = [r + 1 for r in res]
        res += tmp
    res = res[:nums + 1]
    return res


if __name__ == '__main__':
    print(countBits(85723))

