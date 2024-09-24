class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        @cache
        def dfs(i):
            if i == len(s):
                return True
            cur = ''
            for j in range(i,len(s)):
                cur += s[j]
                if cur in words:
                    if dfs(j+1):
                        return True
            return False
        return dfs(0)