class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        numL = index
        numR = n-index-1  

        def count(m, d):
            if m > d:
                return ((m+m-d)*(d+1))//2
            else:
                return (m*(m+1))//2 + d-m+1

        def check(m):
            left = count(m, numL)
            right = count(m, numR)
            
            return left+right-m <= maxSum
            
        l, r = 1, maxSum
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
        