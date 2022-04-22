# Time: O(N/K) where N is the number of unique key-value pairs in map and K is the number of buckets in map.
# Space: O(N + K).
class MyHashMap:
    def __init__(self):
        self.map = [[]]
        self.count = 0
        self.LOAD_FACTOR = 1

    def put(self, key: int, value: int) -> None:
        if (self.count / len(self.map)) >= self.LOAD_FACTOR:
            newMap = [[] for i in range(2*len(self.map))]
            for i in range(len(self.map)):
                for k, v in self.map[i]:
                    newIndex = k % len(newMap)
                    newMap[newIndex].append((k, v))
            self.map = newMap
        
        index = key % len(self.map)
        for i in range(len(self.map[index])):
            if key == self.map[index][i][0]:
                self.map[index][i] = (key, value)
                return
        
        self.map[index].append((key, value))
        self.count += 1

    def get(self, key: int) -> int:
        index = key % len(self.map)
        for k, v in self.map[index]:
            if key == k:
                return v
        return -1        

    def remove(self, key: int) -> None:
        index = key % len(self.map)
        for i in range(len(self.map[index])):
            if key == self.map[index][i][0]:
                self.map[index].pop(i)
                self.count -= 1
                return

myHashMap = MyHashMap()
myHashMap.put(1, 1) # The map is now [[1,1]]
myHashMap.put(2, 2) # The map is now [[1,1], [2,2]]
print(myHashMap.get(1))    # return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3))    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2))    # return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2) # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))    # return -1 (i.e., not found), The map is now [[1,1]]
