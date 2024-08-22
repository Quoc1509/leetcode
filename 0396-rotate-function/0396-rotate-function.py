class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        s = sum(nums)
        res = 0
        n = len(nums)
        for i in range(n):
            res += (i*nums[i])
        temp = res
        for i in range(n):
           
            res = max(res, temp)
            temp = temp - (nums[n-1-i]*(n-1))
            temp += (s - nums[n-i-1])
        return res
