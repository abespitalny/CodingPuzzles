'''
You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.
'''
from leetcode import *

# Time: O(n), Space: O(1).
def max_profit(prices: List[int], fee: int) -> int:
    # Final maximum amount of profit.
    profit = 0
    # Max. profit that could change whether there is a small drop and then a larger upswing in the market.
    tmp_profit = 0
    past_price = prices[0]
    # Last low where there was a significant drop in the market.
    last_low = prices[0]
    # The net amount the stock has dropped in a bearish market.
    net_drop = 0
    for i in range(1, len(prices)):
        cur_price = prices[i]
        # Sideways movement:
        if cur_price == past_price:
            continue
        # Stock has dropped:
        elif cur_price < past_price:
            net_drop += (cur_price - past_price)
            # If current price is lower than last low, then update last low:
            if cur_price < last_low:
                last_low = cur_price
            # A drop more than or equal to the fee is considered a significant drop.
            if (-net_drop >= fee) and (tmp_profit > 0):
                # Reset the last low even if the current price is not lower than the last lowest price.
                last_low = cur_price
                # Add the temporary max. profit to the final max. profit
                profit += tmp_profit
                # Reset the temporary max. profit since there was a sizable downturn in the market.
                tmp_profit = 0
        else:
            net_profit = cur_price - last_low - fee
            # Update the temporary max. profit:
            if net_profit > tmp_profit:
                tmp_profit = net_profit
                # Set net_drop to 0 if we are in an up trend.
                net_drop = 0
            # Add back any upward movement after the market had a drop in an overall up trend market.
            elif (net_drop < 0) and (tmp_profit > 0):
                net_drop += (cur_price - past_price)
        past_price = cur_price
    return (profit + tmp_profit)

# Recurrence relation: dp[i] = (max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee), max(dp[i - 1][1], dp[i - 1][0] - prices[i]))
# This is a very concise and clever Leetcode solution that does what I did in two lines!
# A really simple DP approach with O(n) time and O(1) space:
def max_profit_v2(prices: List[int], fee: int) -> int:
    dp = [0, -prices[0]]
    for i in range(1, len(prices)):
        dp[0] = max(dp[0], dp[1] + prices[i] - fee)
        dp[1] = max(dp[1], dp[0] - prices[i])
    return dp[0]


# Greedy approach solution from Leetcode. This is similar to my solution but much simpler.
def max_profit_v3(prices: List[int], fee: int) -> int:
        profit = 0
        minimum = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                profit += prices[i] - fee - minimum
                minimum = prices[i] - fee
        return profit


assert max_profit(prices = [1,3,2,8,4,9], fee = 2) == 8
assert max_profit(prices = [1,3,7,5,10,3], fee = 3) == 6

assert max_profit_v2(prices = [1,3,2,8,4,9], fee = 2) == 8
assert max_profit_v2(prices = [1,3,7,5,10,3], fee = 3) == 6


assert max_profit_v3(prices = [1,3,2,8,4,9], fee = 2) == 8
assert max_profit_v3(prices = [1,3,7,5,10,3], fee = 3) == 6
