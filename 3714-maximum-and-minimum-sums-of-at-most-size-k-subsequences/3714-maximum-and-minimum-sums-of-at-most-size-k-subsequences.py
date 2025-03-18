class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        N = 10**9+7        
        nums.sort()
        def CountSum(arr):
            dp = [[0] * len(arr) for _ in range(k)]
            res = 0
            for L in range(k):
                pre = 0
                for i in range(len(arr)):
                    if L == 0:
                        dp[L][i] = 1
                        res += arr[i]
                    else:
                        
                        if i >= L:
                            dp[L][i] = pre
                            res += dp[L][i] * arr[i]
                        pre += dp[L-1][i]
            
            return res % N

        return (CountSum(nums) + CountSum(nums[::-1]))%N
        # print(dpMax)