from typing import List

# Assume prices is a non-empty list.
def max_profit(prices: List[int]) -> int:
    prices_size = len(prices)
    if prices_size < 2:
        return 0

    past_price = prices[0]
    profit = 0
    for i in range(1, prices_size):
        cur_price = prices[i]
        if past_price < cur_price:
            profit += (cur_price - past_price)
        past_price = cur_price
    return profit

print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([1, 2, 3, 4, 5]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([]))

