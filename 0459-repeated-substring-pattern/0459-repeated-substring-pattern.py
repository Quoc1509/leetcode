def KMP(s):
    res = [0] * len(s)
    for i in range(1, len(s)):
        j = res[i-1]
        while j > 0 and s[i] != s[j]:
            j = res[j-1]
        if s[i] == s[j]:
            res[i] = j + 1
    return res
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        arr = KMP(s)
        num = arr[-1]
        
        return num > 0 and len(s) % (len(s) - num) == 0