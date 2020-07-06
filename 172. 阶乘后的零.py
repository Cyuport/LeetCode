def trailingZeroes(n: int) -> int:
    return 0 if n ==0 else n//5 + trailingZeroes(n//5) #质因数分解后每1个5会贡献1个0，又25=5x5，相当于每5个5需要多计一个0

if __name__ == '__main__':
    print(trailingZeroes(31))