class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        mp = defaultdict(int)
        for i in range(len(arr)):
            mp[arr[i]] = i
        # @cache
        # def dp(i1, i2):
        #     print(i1, i2)
        #     if i2 >= len(arr):
        #         return 0
        #     res = dp(i1,i2+1)
        #     temp = arr[i1]+arr[i2]
        #     if temp in mp:
        #         res = max(res, dp(i2, mp[temp])+1)
        #     return res
        # ans = 0
        # for i in range(len(arr)-1):
        #     ans = max(ans, dp(i, i+1))
        # return ans if ans == 0 else ans + 2
        dp = defaultdict(int)
        res = 0
        for i in range(len(arr)):
            for j in range(i-1, -1, -1):
                if arr[i] - arr[j] >= arr[j]:
                    break
                if arr[i]-arr[j] in mp:
                    
                    dp[(arr[i], arr[j])] = max(dp[(arr[i], arr[j])], dp[(arr[j], arr[i]-arr[j])] + 1)
                    res = max(res, dp[(arr[i], arr[j])])
                     
        return res + 2 if res > 0 else res