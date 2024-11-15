class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def check(m):
            count = 0
            for i in time:
                count += m//i
            return count >= totalTrips

        l, r = 0, 10000000000000000 
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l