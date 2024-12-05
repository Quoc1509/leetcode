class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        
        @cache
        def dp(i, o1, o2):
            if i >= len(nums):
                return 0
            temp = nums[i]
            res1, res2, res3, res4 = inf, inf, inf, inf
            if nums[i] >= k and o2 >0:
                res1 = dp(i+1, o1, o2-1) + (nums[i] - k)
            if o1 > 0:
                res2 = dp(i+1, o1-1, o2) + ceil(nums[i]/2)
            if o1 > 0 and o2 > 0:
                if ceil(nums[i]/2)>=k:
                    res3 = dp(i+1, o1-1, o2-1) + (ceil(nums[i]/2)-k)
                if nums[i] >= k:
                    res4 = dp(i+1, o1-1, o2-1) + ceil((nums[i]-k)/2)
            res5 = dp(i+1, o1, o2) + nums[i]
            return min(res1, res2, res3, res4, res5)
        return dp(0, op1, op2)