class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res, l = 0, 0
        mp = defaultdict(int)
        for r in range(len(s)):
            mp[s[r]] += 1
            while all(mp[c] > 0 for c in 'abc'):
                res += len(s)-r
                mp[s[l]] -= 1
                l += 1

        return res
            