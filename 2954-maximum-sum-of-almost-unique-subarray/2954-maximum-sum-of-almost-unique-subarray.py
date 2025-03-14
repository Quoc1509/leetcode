class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        mp = defaultdict(int)
        res, total = 0, 0
        for i in range(k):
            total += nums[i]
            mp[nums[i]] += 1
        if len(mp) >= m:
            res = max(res, total)
        for r in range(k, len(nums)):
            
            total -= nums[r-k]
            mp[nums[r-k]] -= 1
            if mp[nums[r-k]] == 0:
                del mp[nums[r-k]]
            total += nums[r]
            mp[nums[r]] += 1
            if len(mp) >= m:
                res = max(res, total)
        return res