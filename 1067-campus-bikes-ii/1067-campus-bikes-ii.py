class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        @cache
        def dfs(ind, visit):
            if ind == len(workers):
                return 0
            res = inf
            for i in range(len(bikes)):
                if (1<<i) & visit:
                    continue
                res = min(res, dfs(ind+1, (1<<i) | visit) + (abs(workers[ind][0] - bikes[i][0]) + abs(workers[ind][1] - bikes[i][1])))
            return res
        return dfs(0, 0)