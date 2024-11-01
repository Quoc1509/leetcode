class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        @cache
        def dfs(visit, num):
            if num == n:
                return 1
            count = 0
            for i in range(10):
                if (1 << i) & visit or (num == 0 and i == 0):
                    continue
                count += dfs((1<<i)|visit, num+1)
            return count+1
        
        return dfs(0, 0)