class Solution:
    def hasSameDigits(self, s: str) -> bool:
        number = list(s)
        i = len(s)
        k = 0
        while i > 2:
            j = 0
            while j < len(s)-k-1:
                number[j] = str((int(number[j]) + int(number[j+1])) % 10)
                j += 1
            k += 1
            i -= 1

        return number[0] == number[1]