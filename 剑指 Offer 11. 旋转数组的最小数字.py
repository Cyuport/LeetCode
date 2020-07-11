def minArray(numbers: [int]) -> int:
    res = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            res = numbers[i]
            break
    return res
