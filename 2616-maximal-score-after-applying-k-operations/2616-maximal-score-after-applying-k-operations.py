class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -num)
        res = 0
        while k:
            num = -heappop(heap)
            res += num
            num = ceil(num/3)
            heappush(heap, -num)
            k -= 1
        return res
