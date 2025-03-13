class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        A = [0] * (len(nums)+1)
        j = 0
        total = 0
        for i in range(len(nums)):
            
            while j < len(queries) and nums[i] - total - A[i] > 0:
                l, r, v = queries[j]
                if r >= i:
                    A[max(i, l)] += v
                    A[r+1] += -v
                j+= 1
            total += A[i]
            # print(nums[i], total)
            
            if nums[i] - total > 0:
                return -1
        return j
