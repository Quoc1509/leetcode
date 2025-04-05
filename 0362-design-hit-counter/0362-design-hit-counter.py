class HitCounter:

    def __init__(self):
        self.mp = {}
        self.mp[0] = 0
        self.arr = [0]
        self.count = 1

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.mp:
            self.arr.append(timestamp)
        self.mp[timestamp] = self.count         
        self.count += 1
        

    def getHits(self, timestamp: int) -> int:
        r = bisect_right(self.arr, timestamp)-1
        l = bisect_right(self.arr, timestamp-300)-1
        if l < 0:
            return self.mp[self.arr[r]]
        return self.mp[self.arr[r]] - self.mp[self.arr[l]]

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)