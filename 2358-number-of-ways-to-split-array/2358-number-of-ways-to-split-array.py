class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)
        left, count = 0, 0
        for i in range(len(nums)-1):
            left += nums[i]
            right -= nums[i]
            # print(left, right)
            if left >= right:
                count += 1
        # print(count)
        return count