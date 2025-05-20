class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0] * (len(nums)+1)
        for a, b in queries:
            diff[a] += 1
            diff[b+1] -= 1
        for i in range(1, len(diff)):
            diff[i] += diff[i-1]
        for i in range(len(nums)):
            if diff[i] < nums[i]:
                return False
        return True