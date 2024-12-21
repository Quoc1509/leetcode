class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        @cache
        def dfs(i, diff):
            if i >= len(rods):
                return 0 if diff == 0 else -inf
            temp = -inf
            if diff >= rods[i]:
                temp = dfs(i+1, diff-rods[i])
            else:
                temp = dfs(i+1, abs(diff-rods[i])) + abs(diff-rods[i])
            
            return max(dfs(i+1, diff+rods[i])+rods[i], temp, dfs(i+1, diff))

        return dfs(0, 0)
            