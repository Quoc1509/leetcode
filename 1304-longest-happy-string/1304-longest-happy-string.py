class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heapq.heappush(heap, [-a, "a"])
        if b > 0:
            heapq.heappush(heap, [-b, "b"])
        if c > 0:
            heapq.heappush(heap, [-c, "c"])
        
        res = ""
        while heap:
            tmp = heapq.heappop(heap)
            if len(res) >= 2 and res[-1] == res[-2] == tmp[1]:
                if not heap:
                    break
                a = heapq.heappop(heap)
                res += a[1]
                a[0] += 1
                if a[0] < 0:
                    heapq.heappush(heap, a)
                heapq.heappush(heap, tmp)
            else:
                res += tmp[1]
                tmp[0] += 1
                if tmp[0] < 0:
                    heapq.heappush(heap, tmp)
        
        return res

