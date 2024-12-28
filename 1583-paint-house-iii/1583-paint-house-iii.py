class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @cache
        def dfs(i, pre_color, group):
            if i >= m:
                if group == target:
                    return 0
                return inf
            if houses[i] != 0:
                return dfs(i+1, houses[i] , group + (houses[i] != pre_color))
            else:
                temp = inf
                for color in range(1, n+1):
                    temp = min(temp, dfs(i+1, color, group+(color != pre_color)) + cost[i][color-1])
                return temp
        res = dfs(0, -1, 0)
        return res if res != inf else -1