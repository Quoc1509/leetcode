class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res, l = 0, 0
        mp = defaultdict(int)
        for r in range(len(s)):
            mp[s[r]] += 1
            while len(mp) == 3:
                res += len(s)-r
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l += 1

        return res
            