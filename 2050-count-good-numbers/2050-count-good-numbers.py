def power(x, n, m):
    res = 1
    while n > 0:
        if n & 1:
            res = (res * x) % m
        n >>= 1
        x = (x*x)%m
    return res

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        odd = n // 2
        even = (n+1)//2
        return (power(5, even, mod)*power(4, odd, mod))%mod


                            