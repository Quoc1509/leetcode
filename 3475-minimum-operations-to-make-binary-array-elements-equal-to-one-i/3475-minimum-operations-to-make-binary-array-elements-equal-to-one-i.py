class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                res += 1
                j = i
                while j < i+3:
                    if nums[j] == 0:
                        nums[j] = 1
                    else:
                        nums[j] = 0
                    j += 1
        return res if sum(nums) == len(nums) else -1