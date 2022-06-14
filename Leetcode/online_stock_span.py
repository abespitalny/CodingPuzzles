'''
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward)
for which the stock price was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
'''
from leetcode import *

class StockSpanner:
    def __init__(self):
        self.stack = [(0, math.inf)]
        self.day = 0

    # Time on average will be O(1).
    # Space: O(n)
    def next(self, price: int) -> int:
        self.day += 1

        while price >= self.stack[-1][1]:
            self.stack.pop()

        span = self.day - self.stack[-1][0]
        
        self.stack.append((self.day, price))
        return span

stockSpanner = StockSpanner()
# Expected: 1
print(stockSpanner.next(100))
# Expected: 1
print(stockSpanner.next(80))
# Expected: 1
print(stockSpanner.next(60))
# Expected: 2
print(stockSpanner.next(70))
# Expected: 1
print(stockSpanner.next(60))
# Expected: 4
print(stockSpanner.next(75))
# Expected: 6
print(stockSpanner.next(85))
