class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = 0
        surfix = sum(nums)
        for i in range(len(nums)):
            if prefix == surfix-prefix-nums[i]:
                return i
            prefix += nums[i]

        return -1