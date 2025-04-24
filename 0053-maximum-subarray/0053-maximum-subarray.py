class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -inf
        total = 0
        for num in nums:
            total += num
            res = max(res, total)
            total = max(0, total)
        return res