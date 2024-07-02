class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)

        def check(candie):
            tmp = 0
            for i in candies:
                tmp += (i // candie)
            if tmp >= k:
                return True
            return False
        
        while l <= r:
            m = (l+r)//2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        return r
        