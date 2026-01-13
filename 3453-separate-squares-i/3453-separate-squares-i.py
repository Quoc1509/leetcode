class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        
        l, r = 0, 10**9
        def check(m):
            upper, lower = 0, 0
            for a,b,c in squares:
                if b + c <= m:
                    lower += c*c
                elif b >= m:
                    upper += c*c
                else:
                    upper += abs(b+c-m)*c
                    lower += abs(m-b)*c
            return upper > lower
        while l <= r-10**-5:
            mid = (l+r)/2
            if check(mid):
                l = mid
            else:
                r = mid
        return r