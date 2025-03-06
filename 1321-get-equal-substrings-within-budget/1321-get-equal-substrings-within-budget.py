class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res, total, l = 0, 0, 0
        for r in range(len(s)):
            total += abs(ord(s[r])-ord(t[r]))
            while total > maxCost:
                total -= abs(ord(s[l])-ord(t[l]))
                l += 1
            res = max(res, r-l+1)
        return res
