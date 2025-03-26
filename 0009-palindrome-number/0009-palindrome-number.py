class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        res = 0
        temp = x
        while temp > 0:
            res += temp % 10
            res *= 10
            temp //= 10
        res //= 10
        return res == x