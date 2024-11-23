class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        res = nums[0]
        for i in range(1, len(nums)):
            res = gcd(res, nums[i])
        return res == 1