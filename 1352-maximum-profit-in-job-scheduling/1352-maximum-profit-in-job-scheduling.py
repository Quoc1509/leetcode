class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        temp = sorted([a, b, c] for a, b, c in zip(startTime, endTime, profit))
        
        @cache
        def dfs(i):
            if i >= len(temp):
                return 0  
            index = bisect_left(temp, [temp[i][1], 0,0])
            res = dfs(index) + temp[i][-1] 
            res = max(res, dfs(i+1))
            return res
        return dfs(0)