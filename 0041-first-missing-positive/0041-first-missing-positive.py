class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            # print(i, nums[i])
            if nums[i] <= 0 or nums[i] == i+1 or nums[i] > len(nums) or nums[i] == nums[nums[i]-1]:
                i += 1
            else:
                temp = nums[i]-1
                nums[i], nums[temp] = nums[temp], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums)+1
