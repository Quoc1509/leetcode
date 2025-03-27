class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        if n < 3:
            return n
        res = 0
        for i in range(3, n+1):
            res = first+second
            first = second
            second = res
        return res