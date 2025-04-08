class TwoSum:

    def __init__(self):
        self.mp = defaultdict(int)

    def add(self, number: int) -> None:
        self.mp[number] += 1

    def find(self, value: int) -> bool:
        for key, item in self.mp.items():
            temp = value-key
            if temp in self.mp:
                if temp == key:          
                    if self.mp[value-key] > 1:
                        return True
                else:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)