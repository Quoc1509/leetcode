class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def dfs(total, i):
            nonlocal res
            res += total
            for j in range(i, len(nums)):
                dfs(total^nums[j], j+1)
        dfs(0, 0)
        return res