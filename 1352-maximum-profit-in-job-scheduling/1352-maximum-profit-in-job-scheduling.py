class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        temp = sorted([a, b, c] for a, b, c in zip(startTime, endTime, profit))
        def search(start, end):
            l, r = start, len(temp)-1
            while l <= r:
                m = (l+r)//2
                if temp[m][0] < end:
                    l = m + 1
                else:
                    r = m - 1
            return l
        @cache
        def dfs(i):                                                                                                     
            if i >= len(temp):
                return 0  
            index = search(i, temp[i][1])
            res = dfs(index) + temp[i][-1] 
            res = max(res, dfs(i+1))
            return res
        return dfs(0)