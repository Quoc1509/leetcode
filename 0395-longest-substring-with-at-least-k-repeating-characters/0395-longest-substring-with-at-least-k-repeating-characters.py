class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        alpha = set(s)
        res = 0
        for i in range(1, len(alpha)+1):
            count = defaultdict(int)
            l = 0
            for r in range(len(s)):
                count[s[r]] += 1
                while len(count) > i:
                    count[s[l]] -= 1
                    if count[s[l]] == 0:
                        del count[s[l]]
                    l += 1
                check = True
                for key, item in count.items():
                    if item < k:
                        check = False
                if check:
                    res = max(res, r - l+1)
       
        return res

            

            
