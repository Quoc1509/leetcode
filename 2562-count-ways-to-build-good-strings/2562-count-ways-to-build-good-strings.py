class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        N = 10**9+7
        @cache
        def dfs(length):
            if length > high:
                return 0
            plus = 0
            if length >= low:
                plus = 1
            return (dfs(length+zero)+dfs(length+one)+plus)%N
        return dfs(0)