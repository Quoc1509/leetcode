class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, k = 0, 0
        
        while i < len(nums):
            j = i+1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            count = min(2, j-i)
            while count > 0:
                nums[k] = nums[i]
                k += 1
                count -= 1
            i = j
        return k