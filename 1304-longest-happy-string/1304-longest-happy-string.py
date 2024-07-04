class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, [-a, "a"])
        if b > 0:
            heapq.heappush(heap, [-b, "b"])
        if c > 0:
            heapq.heappush(heap, [-c, "c"])
        
        res = []
        while heap:
            first_count, first_char = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == first_char:
                if not heap:
                    break
                second_count, second_char = heapq.heappop(heap)
                res.append(second_char)
                second_count += 1
                if second_count < 0:
                    heapq.heappush(heap, [second_count, second_char])
                heapq.heappush(heap, [first_count, first_char])
            else:
                res.append(first_char)
                first_count += 1
                if first_count < 0:
                    heapq.heappush(heap, [first_count, first_char])
        
        return "".join(res)

