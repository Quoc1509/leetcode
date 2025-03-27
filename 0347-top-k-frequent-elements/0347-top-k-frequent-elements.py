class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key, value in count.items():
            heappush(heap, (value, key))
            if len(heap) > k:
                heappop(heap)
        return [b for a, b in heap]