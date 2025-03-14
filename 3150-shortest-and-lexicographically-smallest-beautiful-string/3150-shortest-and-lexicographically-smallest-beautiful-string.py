class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = ''
        maxF, l, count = len(s), 0, 0
        for r in range(len(s)):
            if s[r] == '1':
                count += 1
            while count >= k:
                if not res:
                    res = s[l:r+1]
                elif (r-l+1) < maxF:
                    res = s[l:r+1]
                elif (r-l+1) == maxF:
                    res = min(res, s[l:r+1])
                maxF = min(maxF, r-l+1)
                if s[l] == '1':
                    count -= 1
                l += 1         
        return res

        
        