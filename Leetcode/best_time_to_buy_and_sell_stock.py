'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
'''
from leetcode import *

# Time: O(n), Space: O(1).
def max_profit(prices: List[int]) -> int:
    prices_size = len(prices)
    if prices_size < 2:
        return 0

    best_profit = 0
    buy = prices[0]
    for i in range(1, prices_size):
        sell = prices[i]
        profit = sell - buy
        if profit < 0:
            buy = sell
        else:
            if profit > best_profit:
                best_profit = profit
    return best_profit

# Alternative solution which makes use of Kadane's algorithm
def max_profit2(prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0

    best = 0
    balance = -prices[0]
    for i in range(1, n):
        balance = max(balance, -prices[i])
        best = max(best, prices[i] + balance)
    return best


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
