class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        @cache
        def dfs(i, diff):
            if i >= len(rods):
                return 0 if diff == 0 else -inf
            temp = -inf
            return max(dfs(i+1, diff+rods[i])+rods[i], dfs(i+1, diff-rods[i]), dfs(i+1, diff))
        
        res = dfs(0, 0)
        # print(res)
        return res
            