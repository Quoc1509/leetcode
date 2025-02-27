class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        total, res = 0, 0

        for num in arr:
            total += num
            res += mp[1-(total%2)]
            mp[total%2] += 1
 
        return res % (10**9+7)
