class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(st):
            if st == "": return True

            for i in wordDict:
                l = len(i)
                temp = st[:l]
                if i == temp:
                    if dfs(st[l:]):
                        return True
            return False
        return dfs(s) 