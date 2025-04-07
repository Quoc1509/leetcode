class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        maxHeap = []
        minHeap = []
        for i in range(len(weights)-1):
            w = weights[i]+weights[i+1]
            heappush(maxHeap, -w)
            heappush(minHeap, w)
            if len(maxHeap) == k:
                heappop(maxHeap)
            if len(minHeap) == k:
                heappop(minHeap)
        print(maxHeap, minHeap)
        return sum(maxHeap)+sum(minHeap)