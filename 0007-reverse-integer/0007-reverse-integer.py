class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        a = abs(x)
        while a > 0:
            num = a % 10
            a = a // 10
            res = res * 10 + num
        if x < 0:
            res *= -1
        return res if -2**31 <= res < 2**31 else 0