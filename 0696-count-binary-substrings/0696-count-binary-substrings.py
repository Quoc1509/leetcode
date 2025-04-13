class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        i = 0
        first, second = 0, 0
        while i < len(s):
            j = i+1
            second = first
            while j < len(s) and s[i] == s[j]:
                j += 1
            first = j-i
            res += min(first, second)
            i = j
        return res
