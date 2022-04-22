# Time: O(N/K) where N is the number of elements in the set and K is the number of buckets.
# Space: O(K + N).
class MyHashSet:
    def __init__(self):
        self.set = [[]]
        self.count = 0
        self.LOAD_FACTOR = 1

    def add(self, key: int) -> None:
        if (self.count / len(self.set)) >= self.LOAD_FACTOR:
            newSet = [[] for i in range(2*len(self.set))]
            for i in range(len(self.set)):
                for j in self.set[i]:
                    newIndex = j % len(newSet)
                    newSet[newIndex].append(j)
            self.set = newSet
        
        index = key % len(self.set)
        if key not in self.set[index]:
            self.set[index].append(key)
            self.count += 1

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        if key not in self.set[index]:
            return

        self.set[index].remove(key)
        self.count -= 1

    def contains(self, key: int) -> bool:
        return (key in self.set[key % len(self.set)])

myHashSet = MyHashSet()
myHashSet.add(1)      # set = [1]
myHashSet.add(2)      # set = [1, 2]
print(myHashSet.contains(1)) # return True
print(myHashSet.contains(3)) # return False, (not found)
myHashSet.add(2)      # set = [1, 2]
print(myHashSet.contains(2)) # return True
myHashSet.remove(2)   # set = [1]
print(myHashSet.contains(2)) # return False, (already removed)
