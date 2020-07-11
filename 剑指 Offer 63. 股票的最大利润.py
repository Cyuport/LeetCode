def maxProfit(prices: [int]) -> int:
    profit = 0
    min = 0
    for p in prices:
        if p > min:
            min = p
    for p in prices:
        if p < min:
            min = p
        if p - min > profit:
            profit = p - min
    return profit

print(maxProfit([7,6,4,3,1]))
