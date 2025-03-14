class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)

        def check(mid):
            count = 0
            extra = 0
            for num in candies:
                count += num//mid

            return count >= k

        while l <= r:
            m = (l+r)//2
            if check(m):
                l = m + 1
            else: 
                r = m - 1
        return r