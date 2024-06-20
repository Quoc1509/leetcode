class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(lambda: inf)
        res = -inf
        total = 0
        for i in nums:
            prefix[i] = min(prefix[i], total)
            total += i
            if i - k in prefix:
                res = max(res, total - prefix[i-k])
            if i + k in prefix:
                res = max(res, total - prefix[i+k])
        return res if res != -inf else 0
