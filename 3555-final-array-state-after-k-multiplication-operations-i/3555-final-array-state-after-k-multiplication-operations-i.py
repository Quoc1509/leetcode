class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, e in enumerate(nums):
            heappush(heap, (e, i))
        while k > 0:
            num, i = heappop(heap)
            num *= multiplier
            heappush(heap, (num, i))
            k -= 1
        heap.sort(key=lambda x: x[1])
        res = []
        for a, b in heap:
            res.append(a)
        return res