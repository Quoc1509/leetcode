class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dfs(i1, i2):
            if i1 >= len(nums1) or i2 >= len(nums2):
                return -inf
            res = max(dfs(i1+1, i2+1) + (nums1[i1] * nums2[i2]), (nums1[i1] * nums2[i2]))
            res = max(res, dfs(i1+1, i2), dfs(i1, i2+1))
            return res
        return dfs(0, 0)