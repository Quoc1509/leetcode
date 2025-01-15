class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        one1 = bin(num1).count('1')
        one2 = bin(num2).count('1')
        print(one1, one2)
        if one2 == one1: return num1
        elif one2 < one1:
            extra = one1-one2
            i = 0
            while extra > 0:
                if num1 & (1<<i):
                    num1 ^= (1<<i)
                    extra -= 1
                i += 1
            return num1
        else:
            if one2 >= len(bin(num1)[2:]):
                return int('1'*one2, 2)
            extra = one2-one1
            i = 0
            while extra > 0:
                if num1 & (1<<i) == 0:
                    num1 |= (1<<i)
                    extra -= 1
                i += 1
            return num1

        return 0