class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        @cache
        def dfs(i, choose):
            if i >= len(values):
                return -inf
            
            if not choose:
                return max(dfs(i+1, True) + (values[i] + i), dfs(i+1, False))
            else:
                return max(dfs(i+1, True), values[i]-i)
        return dfs(0, False)
