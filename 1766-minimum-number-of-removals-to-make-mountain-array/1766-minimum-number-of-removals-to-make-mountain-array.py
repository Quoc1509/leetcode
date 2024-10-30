
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        L = [0] * len(nums)
        temp = []
        for i in range(len(nums)):
            ind = bisect_left(temp, nums[i])
            if ind == len(temp):
                temp.append(nums[i])
            else:
                temp[ind] = nums[i]
            L[i] = len(temp)
        temp = []
        R = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            ind = bisect_left(temp, nums[i])
            if ind == len(temp):
                temp.append(nums[i])
            else:
                temp[ind] = nums[i]
            R[i] = len(temp)
        longest = 0
        for i in range(1,len(nums)-1):
            if L[i] > 1 and R[i] > 1:
                longest = max(longest, L[i]+R[i]-1)
        # print(L, R)
        return len(nums) - longest