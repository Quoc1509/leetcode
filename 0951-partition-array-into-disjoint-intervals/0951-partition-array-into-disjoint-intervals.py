class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left, right = [-inf]*len(nums), [inf]*len(nums)
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, len(nums)):
            left[i] = max(nums[i], left[i-1])
        for i in range(len(nums)-2, -1, -1):
            right[i] = min(nums[i], right[i+1])
        print(left, right)
        for i in range(len(nums)-1):
            if left[i] <= right[i+1]:
                return i+1

        return len(nums)-1
