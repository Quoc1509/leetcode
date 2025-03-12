class Solution:
    def longestSubstring(self, s: str, k: int) -> int: 
        temp  = set(s)
        res = 0
        for i in range(len(temp)+1):
            mp = defaultdict(int)
            l = 0
            for r in range(len(s)):
                mp[s[r]] += 1
                while len(mp) > i:
                    mp[s[l]] -= 1
                    if mp[s[l]] == 0:
                        del mp[s[l]]
                    l += 1
                    
                valid = True
                for key, item in mp.items():
                    if item < k:
                        valid = False
                if valid:
                    res = max(res, r-l+1)
        return res

            

            
