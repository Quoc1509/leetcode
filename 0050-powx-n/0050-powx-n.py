class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1
        # def dfs(n):
        #     if n == 1:
        #         return x
        #     res = dfs(n//2)

        #     return res * res if n % 2 == 0 else res*res*x
        # res = dfs(abs(n))
        # if n < 0:
        #     return 1/res
        # return res

        a = abs(n)
        res = 1
        while a > 0:
            if a & 1:
                res *= x
            a >>= 1
            x *= x
        if n < 0:
            return 1/res
        return res