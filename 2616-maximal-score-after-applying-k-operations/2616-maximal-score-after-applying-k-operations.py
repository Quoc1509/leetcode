class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        res = 0
        for _ in range(k):
            temp = heapq.heappop(heap)
            res += (-temp)
            heapq.heappush(heap, -(ceil((-temp)/3))) 
        return res