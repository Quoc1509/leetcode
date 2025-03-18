
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, res = 0, 0
        total = 0

        for r in range(len(nums)):
            
            while (total & nums[r]) != 0:
                
                total ^= nums[l]
                l += 1
            total |= nums[r]
            
            res = max(res, r - l + 1)

        return res
                