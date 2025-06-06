class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j = 0, 1
        k = 0
        N = len(s)
        while j + k < N:
            if s[i+k] == s[j+k]:
                k += 1
            elif s[i+k] < s[j+k]:
                i = max(i+k+1, j)
                j = i + 1
                k = 0
            else:
                j += k + 1
                k = 0
        return s[i:]