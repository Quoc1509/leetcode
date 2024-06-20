class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)

        def check(mid):
            res = 0
            for i in quantities:
                res += ceil(i/mid)
            if res > n:
                return True
            return False

        while l <= r:
            m = (l+r)//2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        return l