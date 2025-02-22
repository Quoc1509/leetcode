class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        # mp = [defaultdict(int) for _ in range(k)]
        # for n in nums:
        #     mp[n%k][n] += 1
        # res = 1
        # for m in mp:
        #     dp0, dp1 = 1, 0
        #     prev = -inf
        #     for a in sorted(m):
        #         v = pow(2, m[a]) - 1
        #         ndp0 = (dp0 + dp1) * v
        #         if a - prev == k:
        #             ndp1 = dp0 * v
        #         else:
        #             ndp1 = (dp0 + dp1) * v
        #         dp0, dp1 = ndp0, ndp1
        #         prev = a
        #     res *= dp0 + dp1
        # return res - 1
        res = [0]
    
        def BT(idx, visit):
            res[0] += 1
            for i in range(idx, len(nums)):
                if visit[nums[i]-k] > 0:
                    continue
                visit[nums[i]] += 1
                BT(i+1, visit)
                visit[nums[i]] -= 1
                
        BT(0, defaultdict(int))
        return res[0]-1