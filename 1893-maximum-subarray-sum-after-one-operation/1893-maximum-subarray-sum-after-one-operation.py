class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        #dp1: max sum of sub array without use operation
        #dp2: max sum of sub array with use operation
        #dp3: max sum of sub array at i

        #dp1[i] = max(dp1[i-1] + nums[i], nums[i])

        #dp2[i] = max(dp1[i-1] + nums[i]*nums[i], dp2[i-1] + nums[i], nums[i]*nums[i])

        #dp3[i] = max(dp1[i-1] + nums[i], nums[i] * nums[i])

        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp3 = [0] * len(nums)
        res = -inf
        for i in range(len(nums)):
            dp1[i] = max(dp1[i-1]+nums[i], nums[i])
            dp2[i] = max(dp1[i-1]+ nums[i]*nums[i], dp2[i-1]+nums[i], nums[i]*nums[i])
            res = max(dp1[i], dp2[i], res)
        return res

