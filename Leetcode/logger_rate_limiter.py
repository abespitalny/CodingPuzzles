'''
Design a logger system that receives a stream of messages along with their timestamps.
Each unique message should only be printed at most every 10 seconds
(i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.
'''
from leetcode import *

# Hashmap approach.
class Logger:
    TIME_WINDOW = 10
    def __init__(self):
        self.hashmap = {}

    # Time: O(1)
    # Space: O(n)
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        prevTimestamp = self.hashmap.get(message, -math.inf)
        if (timestamp - prevTimestamp) < self.TIME_WINDOW:
            return False

        self.hashmap[message] = timestamp
        return True

# Queue + set approach.
class Logger2:
    TIME_WINDOW = 10
    def __init__(self):
        self.queue = deque()
        self.hashset = set()

    # Time: O(n) but amortized O(1) for n calls.
    # Space: O(n)
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while len(self.queue) != 0:
            prevTimestamp, msg = self.queue[0]
            if timestamp - prevTimestamp < self.TIME_WINDOW:
                break

            self.queue.popleft()
            self.hashset.remove(msg)

        if message in self.hashset:
            return False
        
        self.queue.append((timestamp, message))
        self.hashset.add(message)
        return True


logger = Logger()
logger2 = Logger2()

assert logger.shouldPrintMessage(1, "foo") == True
assert logger2.shouldPrintMessage(1, "foo") == True
assert logger.shouldPrintMessage(2, "bar") == True
assert logger2.shouldPrintMessage(2, "bar") == True
assert logger.shouldPrintMessage(3, "foo") == False
assert logger2.shouldPrintMessage(3, "foo") == False
assert logger.shouldPrintMessage(8, "bar") == False
assert logger2.shouldPrintMessage(8, "bar") == False
assert logger.shouldPrintMessage(10, "foo") == False
assert logger2.shouldPrintMessage(10, "foo") == False
assert logger.shouldPrintMessage(11, "foo") == True
assert logger2.shouldPrintMessage(11, "foo") == True
