class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        l = 0
        res = 0
        mp = defaultdict(int)
        for r in range(len(s)):
            mp[s[r]] += 1
            while mp[s[r]] > 1:
                mp[s[l]] -= 1 
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l += 1
            if len(mp) >= k:
                # print(mp)
                res += 1
        return res