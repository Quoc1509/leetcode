class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for num in gifts:
            heappush(heap, -num)
        while k > 0:
            num = heappop(heap)
            n = floor(sqrt(-num))
            heappush(heap, -n)
            k -= 1 
        return -sum(heap)