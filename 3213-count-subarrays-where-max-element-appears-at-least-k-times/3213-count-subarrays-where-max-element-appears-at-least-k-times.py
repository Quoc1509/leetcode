class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count  = 0
        l, res = 0, 0
        maxNum = max(nums)
        for r in range(len(nums)):
            if nums[r] == maxNum:
                count += 1
            while count >= k:
                if nums[l] == maxNum:
                    count -= 1
                l += 1
                res += len(nums) - r
        return res