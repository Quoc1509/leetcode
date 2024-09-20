class RandomizedSet:

    def __init__(self):
        self.store = defaultdict(int)
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        self.store[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False
        if self.arr and self.arr[-1] == val:
            self.arr.pop()
            del self.store[val]
            return True
        
        index = self.store[val]
        self.arr[-1], self.arr[index] = self.arr[index], self.arr[-1]
        self.arr.pop()
        self.store[self.arr[index]] = index
        del self.store[val]
        return True

    def getRandom(self) -> int:
    
        random_index = random.randint(0, len(self.arr)-1)
        # print(self.arr, self.store, random_index)
        return self.arr[random_index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()