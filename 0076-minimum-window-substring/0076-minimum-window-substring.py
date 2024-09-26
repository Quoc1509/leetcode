class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return s
        start, end = -1, len(s)
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
                if end-start > (r-l):
                    start, end = l, r

                mp[s[l]] -= 1
                l += 1
                
        return s[start: end+1] if start > -1 else ''

