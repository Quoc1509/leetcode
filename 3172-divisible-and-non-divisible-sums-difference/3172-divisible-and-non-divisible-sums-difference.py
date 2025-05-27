class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total = n*(n+1)//2
        extra = n // m
        num2 = m*(extra*(extra+1)//2)
        num1 = total - num2
        return num1-num2