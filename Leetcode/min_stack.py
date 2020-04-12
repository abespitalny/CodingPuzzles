'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        # Append is O(1).
        stack = self.stack
        if len(stack) == 0:
            stack.append((x, x))
        else:
            stack.append((x, min(x, stack[-1][1])))

    def pop(self) -> None:
        # Popping the last element, i.e. the top of the stack, is O(1).
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())
min_stack.pop()
print(min_stack.top())
print(min_stack.getMin())

min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-1)
print(min_stack.getMin())
print(min_stack.top())
min_stack.pop()
print(min_stack.getMin())
