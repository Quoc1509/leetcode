from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.sortList = SortedList()

    def addNum(self, num: int) -> None:
        self.sortList.add(num)

    def findMedian(self) -> float:
        l = len(self.sortList)
        if l %2 != 0:
            return self.sortList[l//2]
        else:
            return (self.sortList[l//2] + self.sortList[(l//2)-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()