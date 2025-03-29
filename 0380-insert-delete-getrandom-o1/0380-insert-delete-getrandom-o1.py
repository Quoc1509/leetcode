class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.mp = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.arr.append(val)
        self.mp[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False

        remove_index = self.mp[val]
        last_num = self.arr[-1]
        self.mp[last_num] = remove_index
        self.arr[remove_index] = last_num
        self.arr.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.arr)-1)
        return self.arr[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()