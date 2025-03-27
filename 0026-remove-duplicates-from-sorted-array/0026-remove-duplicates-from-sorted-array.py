class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j < len(nums):
            nums[i] = nums[j]
            k = j + 1
            while k < len(nums) and nums[i] == nums[k]:
                k += 1
            j = k
            i += 1
        return i