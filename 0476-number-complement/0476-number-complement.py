class Solution:
    def findComplement(self, num: int) -> int:
        res, count = 0, 0
        while num > 0:
            temp = num % 2
            num = num // 2
            if temp == 0:
                res += pow(2, count)
            count += 1
        return res