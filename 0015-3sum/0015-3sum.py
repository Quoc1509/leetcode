class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        N = len(nums)
        for i in range(N):
            left, right = 0, N-1
            while left < i and right > i:
                if left > 0 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right < N-1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue
                if nums[left] + nums[i] + nums[right]== 0:
                    temp = (nums[left], nums[i], nums[right])
                    res.add(temp)
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res