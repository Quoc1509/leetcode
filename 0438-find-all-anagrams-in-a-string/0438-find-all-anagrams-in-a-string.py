class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mp = Counter(p)
        ms = defaultdict(int)
        l = 0
        res = []
        for r in range(len(s)):
            ms[s[r]] += 1
            while ms[s[r]] > mp[s[r]]:
                ms[s[l]] -= 1
                l += 1
            if r-l+1 == len(p):
                res.append(l)
        return res