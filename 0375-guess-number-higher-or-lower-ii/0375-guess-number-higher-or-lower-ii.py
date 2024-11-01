class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @cache
        def dfs(start, end):
            if start == end:
                return 0 
            if end-start < 2:
                return start
            num = inf
            for i in range(start+1, end):
                num = min(num, max(dfs(start, i-1), dfs(i+1, end))+i)
            return num 
        return dfs(1, n)

        
