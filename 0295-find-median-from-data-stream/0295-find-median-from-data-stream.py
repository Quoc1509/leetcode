class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap and not self.maxHeap:
            heappush(self.minHeap, num)
        elif self.minHeap and self.minHeap[0] <= num:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -num)
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            temp = heappop(self.minHeap)
            heappush(self.maxHeap, -temp)
        elif len(self.minHeap) + 1 <= len(self.maxHeap):
            temp = heappop(self.maxHeap)
            heappush(self.minHeap, -temp)

    def findMedian(self) -> float:
        if (len(self.maxHeap) + len(self.minHeap)) % 2 != 0:
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0])/ 2
        
        