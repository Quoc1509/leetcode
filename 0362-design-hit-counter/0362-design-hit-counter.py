class HitCounter:

    def __init__(self):
        self.mp = {}
        self.mp[0] = 0
        self.arr = [0]
        self.count = 1

    def hit(self, timestamp: int) -> None:
        self.mp[timestamp] = self.count
        self.arr.append(timestamp)
        self.count += 1
        # print(self.mp)

    def getHits(self, timestamp: int) -> int:
        index1 = bisect_right(self.arr, timestamp)
        index2 = bisect_right(self.arr, timestamp-300)
        # print(self.mp, self.arr, index1, index2)
        if index2 <= 0:
            return self.mp[self.arr[index1-1]]
        return self.mp[self.arr[index1-1]]-self.mp[self.arr[index2-1]]


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)