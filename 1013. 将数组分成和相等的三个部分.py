def canThreePartsEqualSum(A: [int]) -> bool:
    sum = 0
    for _ in A:
        sum += _
    if sum % 3:
        return False
    sum //= 3
    count = 0
    num = 0
    for _ in A:
        count += _
        if count == sum:
            count = 0
            num += 1
    if num == 3:
        return True
    return False


if __name__ == '__main__':
    print(canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))
