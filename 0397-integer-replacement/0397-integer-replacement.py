class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1: return 0
        count = 0
        while n > 2:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3: return count + 2
                temp = (n + 1) // 2
                
                if temp % 2 == 0:
                    n += 1
                else: n -= 1
            count += 1
        return count + 1