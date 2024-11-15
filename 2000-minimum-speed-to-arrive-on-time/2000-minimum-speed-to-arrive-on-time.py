class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def check(mid):
            res = 0
            for d in range(len(dist)-1):
                res += ceil(dist[d]/mid)
            res += dist[-1]/mid
            # print(res)
            return res <= hour
        if ceil(hour) < len(dist): return -1
        l, r = 1, 10**9
        while l <= r:
            m = (l+r)//2
            # print(l, r, m)

            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l if l > 0 else -1
            