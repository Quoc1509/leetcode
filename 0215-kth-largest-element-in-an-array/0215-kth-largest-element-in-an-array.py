class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for i in nums:
            if len(heap) < k:
                heapq.heappush(heap, i)
            else:
                if i > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, i)
        return heap[0]