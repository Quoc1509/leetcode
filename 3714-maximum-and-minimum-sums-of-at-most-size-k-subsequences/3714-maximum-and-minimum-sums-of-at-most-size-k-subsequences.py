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
                    else:
                        if i >= L:
                            dp[L][i] = pre
                            
                        pre += dp[L-1][i]
                    res = (res + dp[L][i] * arr[i]) %N
                    
            return res % N

        return (CountSum(nums) + CountSum(nums[::-1]))%N
        # print(dpMax)