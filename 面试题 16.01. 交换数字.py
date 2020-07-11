def swapNumbers(number: [int]) -> [int]:
    number[0] ^= number[1]
    number[1] ^= number[0]
    number[0] ^= number[1]
    return number