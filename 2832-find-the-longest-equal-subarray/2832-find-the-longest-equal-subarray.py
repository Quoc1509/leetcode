class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        res, l = 0, 0
        mp = defaultdict(list)
        for i, e in enumerate(nums):
            mp[e].append(i)
        # print(mp)
        res = 1
        for key, item in mp.items():
            l = 1
            diff = 0
            for r in range(1, len(item)):                
                diff += item[r] - item[r-1] - 1
                while diff > k:
                    diff -= item[l] - item[l-1] - 1
                    l += 1
                res = max(res, r-l+2) 
        return res