class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s
        res = ''
        temp = inf
        count = Counter(t)
        l = 0
        mp = defaultdict(int)
        def compare(mp):
            for key, item in count.items():
                if mp[key] < item:
                    return False

            return True

        for r in range(len(s)):
            
            mp[s[r]] += 1
            while compare(mp):
                if temp > (r-l+1):
                    res = s[l:r+1]
                    temp = len(res)

                mp[s[l]] -= 1
                l += 1
                
        return res

