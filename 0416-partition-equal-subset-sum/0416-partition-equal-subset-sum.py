class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        maxSum = sum(nums)
        if maxSum % 2 == 1:
            return False
        @cache
        def dfs(i, total):
            if total == maxSum // 2:
                return True
            if i >= len(nums) or total > maxSum//2: 
                return False
            
            return dfs(i+1, total + nums[i]) or dfs(i+1, total)
                    
        return dfs(0, 0)