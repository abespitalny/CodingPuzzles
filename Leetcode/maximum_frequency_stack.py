'''
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:
    - FreqStack() constructs an empty frequency stack.
    - void push(int val) pushes an integer val onto the top of the stack.
    - int pop() removes and returns the most frequent element in the stack.

If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
'''
from leetcode import *

# Heap approach
class FreqStack:
    def __init__(self):
        self.top = 0
        self.heap = []
        self.freq = defaultdict(int)

    # Time: O(log(n))
    # Space: O(n)
    def push(self, val: int) -> None:
        self.freq[val] += 1
        heapq.heappush(self.heap, (-self.freq[val], -self.top, val))
        self.top += 1

    # Time: O(log(n))
    # Space: O(n)
    def pop(self) -> int:
        _, _, val = heapq.heappop(self.heap)
        self.freq[val] -= 1
        return val

# From Leetcode, stack of stacks approach. O(1) time for both operations with O(n) space. Beautiful!
class FreqStack2:
    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        freq = self.freq[val] + 1
        self.freq[val] = freq
        if freq > self.maxfreq:
            self.maxfreq = freq

        self.group[freq].append(val)

    def pop(self) -> int:
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return val

freqStack = FreqStack()
freqStack2 = FreqStack2()

freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)

freqStack2.push(5)
freqStack2.push(7)
freqStack2.push(5)
freqStack2.push(7)
freqStack2.push(4)
freqStack2.push(5)

assert freqStack.pop() == 5
assert freqStack.pop() == 7
assert freqStack.pop() == 5
assert freqStack.pop() == 4

assert freqStack2.pop() == 5
assert freqStack2.pop() == 7
assert freqStack2.pop() == 5
assert freqStack2.pop() == 4
