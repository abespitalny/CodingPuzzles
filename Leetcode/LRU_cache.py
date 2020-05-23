from leetcode import *

class Node:
    def __init__(self, val: Any):
        self.val = val
        self.prev_ptr = None
        self.next_ptr = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # This is O(1).
    def enqueue(self, node: Node) -> None:
        head = self.head
        if head is None:
            self.head = node
            self.tail = node
        else:
            node.prev_ptr = None
            node.next_ptr = head
            head.prev_ptr = node
            self.head = node
        self.size += 1

    # This is O(1).
    def dequeue(self) -> Node:
        if self.size == 0:
            return None

        tail = self.tail
        if self.head == tail:
            self.head = None
            self.tail = None
        else:
            prev_node = tail.prev_ptr
            self.tail = prev_node
            prev_node.next_ptr = None
        self.size -= 1
        return tail

    # Deletes the node where it occurs in the queue and enqueues it. This is O(1).
    # I am assuming that the node is a valid node in the queue.
    def del_enqueue(self, node: Node) -> None:
        if self.head == node:
            return
        elif self.tail == node:
            self.enqueue(self.dequeue())
        else:
            # Delete the node from somewhere in the middle of the queue.
            node.prev_ptr.next_ptr = node.next_ptr
            node.next_ptr.prev_ptr = node.prev_ptr
            self.size -= 1
            self.enqueue(node)

# Get and put operations are both O(1).
class LRUCache:
    # The cache is initialized with a positive capacity.
    def __init__(self, capacity: int):
        self.queue = Queue()
        self.table = {}
        self.capacity = capacity

    # Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    def get(self, key: int) -> int:
        # Lookup is generally O(1) for hash tables.
        val_ptr = self.table.get(key, None)
        if val_ptr is None:
            return -1
        # Delete item from wherever it currently is in the queue and add it to the front of the queue
        # since this value is the most recently used one.
        self.queue.del_enqueue(val_ptr)
        return val_ptr.val[1]

    # Set or insert the value if the key is not already present.
    # When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
    def put(self, key: int, value: int) -> None:
        table = self.table
        queue = self.queue

        val_ptr = table.get(key, None)
        # Key is not in the table, so a new item must be added to the cache:
        if val_ptr is None:
            # Evict the least recently used item if capacity has been reached.
            if queue.size == self.capacity:
                evicted_node = queue.dequeue()
                # Deleting an item from a hash table is generally O(1).
                del table[evicted_node.val[0]]
            # Enqueue this new item and add it to the table.
            new_item = Node([key, value])
            queue.enqueue(new_item)
            table[key] = new_item
        else:
            # Update the value in the value pointer.
            val_ptr.val[1] = value
            # Update the queue so it reflects that this is the most recently used item.
            queue.del_enqueue(val_ptr)


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
# Prints 1:
print(cache.get(1))
# Evicts key 2:
cache.put(3, 3)
# Prints -1 (not found):
print(cache.get(2))
# Evicts key 1:
cache.put(4, 4)
# Prints -1 (not found):
print(cache.get(1))
# Prints 3:
print(cache.get(3))
# Prints 4
print(cache.get(4))

cache = LRUCache(3)
cache.put(1, 1)
cache.put(2, 2)
cache.put(3, 3)
# Evicts key 1:
cache.put(4, 4)
# Prints 4:
print(cache.get(4))
# Prints 3
print(cache.get(3))
# Prints 2
print(cache.get(2))
# Prints -1
print(cache.get(1))
# Evicts key 4
cache.put(5, 5)
# Prints -1
print(cache.get(1))
# Prints 2
print(cache.get(2))
# Prints 3
print(cache.get(3))
# Prints -1
print(cache.get(4))
# Prints 5
print(cache.get(5))
