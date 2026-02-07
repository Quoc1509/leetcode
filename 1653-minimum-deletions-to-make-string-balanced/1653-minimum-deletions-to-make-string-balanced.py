class Solution:
    def minimumDeletions(self, s: str) -> int:
        m = Counter(s)
        t = defaultdict(int)
        res = max(m['a'], m['b'])
        for c in s:
            t[c] += 1
            res = max(res, t['a'] + m['b'] - t['b'])
        return len(s) - res
        