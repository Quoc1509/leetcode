class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # dp1[i]: maximum sum of subarray end at i without del one
        # dp2[i]: maximim sum of subarray end at i after del one
        
        dp1 = -inf
        dp2 = -inf
        res = -inf
        for num in arr:
            ndp1 = max(num, dp1+num)
            ndp2 = max(dp1, dp2 + num)
            res = max(res, ndp1, ndp2)
            dp2 = ndp2
            dp1 = ndp1
        return res