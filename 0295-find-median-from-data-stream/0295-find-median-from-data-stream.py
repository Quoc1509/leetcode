from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.heapMax = []
        self.heapMin = []

    def addNum(self, num: int) -> None:
        if not self.heapMax and not self.heapMin:
            heappush(self.heapMin, num)
        elif self.heapMin and self.heapMin[0] <= num:
            heappush(self.heapMin, num)
        else:
            heappush(self.heapMax, -num)

        if len(self.heapMin) > len(self.heapMax) + 1:
            temp = heappop(self.heapMin)
            heappush(self.heapMax, -temp)
        elif len(self.heapMin) + 1 <= len(self.heapMax):
            temp = heappop(self.heapMax)
            heappush(self.heapMin, -temp)


    def findMedian(self) -> float:
        if (len(self.heapMax) + len(self.heapMin)) % 2 != 0:

            return self.heapMin[0]
        else:
            return (self.heapMin[0] - self.heapMax[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()