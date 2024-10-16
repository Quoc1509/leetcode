class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a > 0:
            heappush(heap, [-a, 'a'])
        if b > 0:
            heappush(heap, [-b, 'b'])
        if c > 0:
            heappush(heap, [-c, 'c'])
        res = ''
        while heap:
            cur = heappop(heap)
            if len(res) > 1 and res[-1] == res[-2] == cur[1]:
                if not heap:
                    break
                temp = heappop(heap)
                res += temp[1]
                temp[0] += 1
                if temp[0] < 0:
                    heappush(heap, temp)
            else:
                res += cur[1]
                cur[0] += 1
            if cur[0] < 0:
                heappush(heap, cur)
        return res