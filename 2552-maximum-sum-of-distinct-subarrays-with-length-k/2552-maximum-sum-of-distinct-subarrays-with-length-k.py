class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        mp = defaultdict(int)
        for i in range(k):
            mp[nums[i]] += 1
            total += nums[i]
        res = total if len(mp) == k else 0
        for i in range(k, len(nums)):
            total -= nums[i-k]
            mp[nums[i-k]] -= 1
            if mp[nums[i-k]] == 0:
                del mp[nums[i-k]]
            total += nums[i]
            mp[nums[i]] += 1
            if len(mp) == k:
                res = max(total, res)
        return res