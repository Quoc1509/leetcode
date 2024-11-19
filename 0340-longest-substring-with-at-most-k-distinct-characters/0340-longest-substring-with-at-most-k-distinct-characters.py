class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        mp = defaultdict(int)
        l, res = 0, 0
        for r in range(len(s)):
            mp[s[r]] += 1
            while len(mp) > k:
                mp[s[l]] -= 1
                if mp[s[l]] == 0:
                    del mp[s[l]]
                l+=1
            res = max(res, r-l+1)
        return res
