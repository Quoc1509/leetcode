class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        res = 0
        temp = x
        while temp > 0:
            num = temp % 10
            res = res * 10 + num
            temp //= 10
        return res == x