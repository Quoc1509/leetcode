class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        l, r = 1, max(quantities)
        def check(mid):
            count = 0
            for num in quantities:
                count += ceil(num / mid)           
            return count > n

        while l <= r:
            m = (l+r)//2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        return l