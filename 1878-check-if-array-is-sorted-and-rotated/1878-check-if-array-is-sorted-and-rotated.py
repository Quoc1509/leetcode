class Solution:
    def check(self, nums: List[int]) -> bool:
        allow = 0 if nums[-1] > nums[0] else 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                allow -= 1
            if allow < 0:
                return False
        return True 