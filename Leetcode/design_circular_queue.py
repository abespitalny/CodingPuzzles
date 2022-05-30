# Array approach
# Time: O(1) for all operations.
# Space: O(n) for all operations.
class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0]*k
        self.head = -1
        self.tail = -1        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        if self.isEmpty():
            self.head = self.tail = 0
            self.queue[0] = value
            return True
        
        self.tail = (self.tail + 1) % len(self.queue)
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        # Delete last element in queue.
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True

        self.head = (self.head + 1) % len(self.queue)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.tail]
        
    def isEmpty(self) -> bool:
        return (self.head == -1)
        
    def isFull(self) -> bool:
        return ((self.tail + 1) % len(self.queue) == self.head)

k = 3
queue = MyCircularQueue(k)
print(queue.enQueue(1))
print(queue.enQueue(2))
print(queue.enQueue(3))
print(queue.enQueue(4))
print(queue.Rear())
print(queue.isFull())
print(queue.deQueue())
print(queue.enQueue(4))
print(queue.Rear())
