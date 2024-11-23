class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        res = nums[0]
        for i in range(1, len(nums)):
            res = gcd(res, nums[i])
        return True if res == 1 else False