class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = 1, sum(weights)


        def check(m):
            count, total = 1, 0
            for i in weights:
                if i >= m:
                    return False
                if total + i == m:
                    total = 0
                    count += 1
                if total + i > m:
                    total = i
                    count += 1
                else:
                    total += i
   
            return count <= days

        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r
