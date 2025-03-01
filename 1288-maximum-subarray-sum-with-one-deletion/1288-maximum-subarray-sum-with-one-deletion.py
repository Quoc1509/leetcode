class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # dp1[i]: maximum sum of subarray end at i without del one
        # dp2[i]: maximim sum of subarray end at i after del one
        
        dp1 = {-1: -inf}
        dp2 = {-1: -inf}
        res = -inf
        for i in range(len(arr)):
            dp1[i] = max(arr[i], dp1[i-1]+arr[i])
            dp2[i] = max(dp1[i-1], dp2[i-1] + arr[i])
            res = max(res, dp1[i], dp2[i])
        return res