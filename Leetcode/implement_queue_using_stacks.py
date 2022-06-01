'''
Implement a first in first out (FIFO) queue using only two stacks.
'''

# Leetcode inspired amortized O(1) solution.
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x: int) -> None:
        if len(self.stack1) == 0:
            self.front = x
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        if len(self.stack2) != 0:
            return self.stack2[-1]
        return self.front

    def empty(self) -> bool:
        return (len(self.stack1) == 0 and len(self.stack2) == 0)


# Original crack at creating an amortized O(1) solution. Peek is inefficient, and I'm shuffling elements from stack1 and stack2 and back.
# However, I was very close to the right idea. The Leetcode inspired solution is above.
class MyQueue2:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        while len(self.stack2) != 0:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

    def pop(self) -> int:
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())

        if len(self.stack2) != 0:
            return self.stack2[-1]

    def empty(self) -> bool:
        return (len(self.stack1) == 0 and len(self.stack2) == 0)
