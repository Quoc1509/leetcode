class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mt = Counter(t)
        ms = defaultdict(int)
        l, res = 0, ''
        start, end = 0, inf
        def check():
            for key, item in mt.items():
                if ms[key] < item:
                    return False
            return True

        for r in range(len(s)):
            ms[s[r]] += 1
            while check():
                if end-start > r-l:
                    start, end = l, r
                    
                ms[s[l]] -= 1
                if ms[s[l]] == 0:
                    del ms[s[l]]
                l += 1
        # print(start, end)
        return s[start:end+1] if end != inf else ''
        