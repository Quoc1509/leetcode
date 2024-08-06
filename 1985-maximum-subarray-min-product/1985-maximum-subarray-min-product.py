class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        res = 0
        
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        stack = []
        for i in range(n+1):
            minNum = 0
            if i < n: minNum = nums[i] 
            while stack and nums[stack[-1]] > minNum:
                j = stack.pop()
                l = stack[-1] if stack else -1
                r = i
                res = max(res, (prefix_sum[r] - prefix_sum[l+1])*nums[j])
            stack.append(i)
        return res % MOD


