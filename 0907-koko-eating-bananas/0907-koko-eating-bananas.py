class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        
        def check(mid):
            count = 0
            for pile in piles:
                count += ceil(pile/mid)
                if count > h:
                    return False
            return True

        while l <= r:
            m = (l+r)//2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l