class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dic = set(dictionary)
        @cache
        def dfs(i):
            if i == len(s):
                return 0
            res = dfs(i+1) + 1
            cur = ''
            for j in range(i,len(s)):
                cur += s[j]
                if cur in dic:
                    res = min(res, dfs(j+1))
            return res
        return dfs(0)
