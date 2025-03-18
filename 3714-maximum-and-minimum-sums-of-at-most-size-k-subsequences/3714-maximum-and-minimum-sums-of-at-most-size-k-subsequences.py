
dp = [[0] * (10**5) for _ in range(70)]
for L in range(70):
    pre = 0
    for i in range(10**5):
        if L == 0:
            dp[L][i] = 1
        else:
            if i >= L:
                dp[L][i] = pre
                
            pre += dp[L-1][i]

for L in range(1, 70):
    for i in range(10**5):

        dp[L][i] += dp[L-1][i]

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        M = 10**9+7
        N = len(nums)        
        nums.sort()
        res = 0
        for i in range(N):
            res = (res + dp[k-1][i] * (nums[i] + nums[N-i-1])) % M    

        return res
        # print(dpMax)