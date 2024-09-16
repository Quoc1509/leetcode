class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(st):
            if st == "": return True
            if st in memo: return memo[st]
            for i in wordDict:
                l = len(i)
                temp = st[:l]
                if i == temp:
                    if dfs(st[l:]):
                        return True
            memo[st] = False
            return memo[st]
        return dfs(s) 