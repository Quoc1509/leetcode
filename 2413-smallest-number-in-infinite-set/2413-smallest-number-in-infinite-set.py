class SmallestInfiniteSet:

    def __init__(self):
        self.nums = set()
        self.heap = []
        self.minNum = 1

    def popSmallest(self) -> int:
        if not self.heap or self.minNum < self.heap[0]:
            num = self.minNum
            self.minNum += 1
            return num
        num = heappop(self.heap)
        self.nums.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num < self.minNum and num not in self.nums:
            self.nums.add(num)
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)