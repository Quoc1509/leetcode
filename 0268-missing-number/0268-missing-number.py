class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        for i, e in enumerate(nums):
            num ^= (i+1)
            num ^= e
        return num