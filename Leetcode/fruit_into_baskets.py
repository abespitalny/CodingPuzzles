'''
You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
    - You only have two baskets, and each basket can only hold a single type of fruit.
      There is no limit on the amount of fruit each basket can hold.

    - Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right.
      The picked fruits must fit in one of your baskets.

    - Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.
'''
from leetcode import *

class Solution:
    # A kind of hybrid greedy / sliding window approach. Basically, we have to find longest continguous sub array with two distinct values.
    # Time: O(n)
    # Space: O(1)
    def totalFruit(self, tree: List[int]) -> int:
        maxFruit = 0
        numFruit = 0
        baskets = [-1, -1]

        for i in range(len(tree)):
            # First basket is empty
            if baskets[0] == -1:
                baskets[0] = i
            # Add to first basket
            elif tree[baskets[0]] == tree[i]:
                baskets[0] = i
            # Second basket is empty
            elif baskets[1] == -1:
                baskets[1] = i
            # Add to second basket
            elif tree[baskets[1]] == tree[i]:
                baskets[1] = i
            # Fruit can't go into either basket
            else:
                maxFruit = max(maxFruit, numFruit)
                minBasketIdx = 0 if baskets[0] < baskets[1] else 1
                numFruit = i - (baskets[minBasketIdx] + 1)
                baskets[minBasketIdx] = i

            numFruit += 1

        return max(maxFruit, numFruit)

solution = Solution()

assert solution.totalFruit([1,2,1]) == 3

assert solution.totalFruit([0,1,2,2]) == 3

assert solution.totalFruit([1,2,3,2,2]) == 4
