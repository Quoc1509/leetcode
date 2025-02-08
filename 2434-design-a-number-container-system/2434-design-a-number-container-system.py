class NumberContainers:

    def __init__(self):
        self.mp = defaultdict(SortedList)
        self.history = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if index not in self.history:
            self.history[index] = number
            self.mp[number].add(index)
        else:
            self.mp[self.history[index]].remove(index)
            self.mp[number].add(index)
            self.history[index] = number
            

    def find(self, number: int) -> int:
        if number not in self.mp or len(self.mp[number]) == 0:
            return -1
        return self.mp[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)