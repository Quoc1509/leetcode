class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = Counter(s)
        def check():
            if count['a'] < k or count['b'] < k or count['c'] < k:
                return False
            return True
        if not check():
            return -1
        l, res = 0, 0
        for r in range(len(s)):
            count[s[r]] -= 1
            while l <= r and not check():

                count[s[l]] += 1
                l += 1
            res = max(res, r-l+1)
        return len(s)-res