class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0: return s
        count = Counter(s)
        heap = []
        for key, item in count.items():
            heappush(heap, (-item, key))
        res = ''
        while heap:
            temp = []
            ok = True
            for i in range(k):
                if not heap:
                    ok = False
                    break
                a, b = heappop(heap)
                res += b
                a += 1
                if a < 0:
                    temp.append((a, b))
            for num, alpha in temp:
                heappush(heap, (num, alpha))
            if not ok: 
                break

        return '' if heap else res


            