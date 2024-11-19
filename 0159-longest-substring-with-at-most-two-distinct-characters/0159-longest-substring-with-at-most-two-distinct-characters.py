class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        mp = defaultdict(int)
        l, res = 0, 0
        for r in range(len(s)):
            mp[s[r]] += 1
            while len(mp) > 2:
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l+=1
            res = max(res, r-l+1)
        return res