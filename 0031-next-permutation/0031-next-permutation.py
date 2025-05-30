class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        i -= 1
        j = i + 1
        while j < len(nums) and nums[i] < nums[j]:
            j += 1
        j-= 1

        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]