class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        @cache
        def dfs(i1, i2):
            if i2 >= len(t):
                return 1
            if i1 >= len(s):
                return 0
            if s[i1] == t[i2]:
                return dfs(i1+1, i2+1) + dfs(i1+1, i2)
            else:
                return dfs(i1+1, i2)
        return dfs(0, 0)