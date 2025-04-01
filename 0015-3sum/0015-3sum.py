class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    r -= 1
                    k = l + 1
                    while k < len(nums) and nums[k] == nums[l]:
                        k += 1
                    l = k
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            i = j
        return res