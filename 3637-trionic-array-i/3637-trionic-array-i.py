class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 0 
        while i < len(nums) - 1 and nums[i] < nums[i + 1]:
            i += 1
        j = len(nums)-1
        while j > 1 and nums[j] > nums[j-1]:
            j -= 1
        if j <= i or i == 0 or j == len(nums)-1:
            return False
        # print(i, j)
        while i < j:
            if nums[i] <= nums[i+1]:
                return False
            i += 1
        return True