class Solution:
    def minimumLength(self, s: str) -> int:
        mp = defaultdict(int)
        res = len(s)
        for c in s:
            mp[c] += 1
            if mp[c] >= 3:
                mp[c] -= 2
                res -= 2
        return res