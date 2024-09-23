class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        res = [inf]
        @cache
        def dfs(remain, start):
            res[0] = min(res[0], remain)
            for word in dictionary:
                l = len(word)
                for i in range(start, len(s)):
                    if word == s[i:i+l]:
                        dfs(remain-l, i+l)
        dfs(len(s), 0)
        return res[0]
