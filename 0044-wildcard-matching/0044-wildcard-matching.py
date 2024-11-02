class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def dfs(i1, i2):
            if i1 == len(s) and i2 == len(p):
                return True
            if i1 >= len(s) and p[i2].isalpha():
                return False
            if i2 >= len(p):
                return False
            if i1 < len(s) and i2 < len(p) and (s[i1] == p[i2] or p[i2] == '?'):
                return dfs(i1+1, i2+1)
            elif p[i2] == '*':
                if i1 < len(s):
                    return dfs(i1, i2+1) or dfs(i1+1, i2) or dfs(i1+1, i2+1)
                else:
                    return dfs(i1, i2+1)
            return False
        return dfs(0, 0)
            
