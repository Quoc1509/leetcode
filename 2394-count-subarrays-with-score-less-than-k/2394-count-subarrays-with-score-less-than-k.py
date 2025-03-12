class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res, l = 0, 0
        product = 0
        for r in range(len(nums)):
            product += nums[r]
            while product * (r-l+1) >= k:
                product -= nums[l]
                l += 1
            res += (r-l+1)
        return res 
        
