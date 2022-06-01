'''
Implement a last-in-first-out (LIFO) stack using only two queues.

Follow-up: Can you implement the stack using only one queue?
'''
from leetcode import *

# Time: O(n) for popping and O(1) for all other operations.
# This solution uses only one queue.
class MyStack:
    def __init__(self):
        self.queue = deque()
        self.back = None        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.back = x

    def pop(self) -> int:
        size = len(self.queue)
        i = 0
        while i < (size - 1):
            if i == (size - 2):
                self.back = self.queue[0]
            self.queue.append(self.queue.popleft())
            i += 1
        
        return self.queue.popleft()

    def top(self) -> int:
        return self.back

    def empty(self) -> bool:
        return (len(self.queue) == 0)
