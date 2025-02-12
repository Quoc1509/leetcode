class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        res = -1
        mp = defaultdict(int)
        for num in nums:
            c = num
            temp = 0
            while c > 0:
                temp += (c % 10)
                c //= 10
            if temp in mp:
                res = max(res, num+mp[temp])
            mp[temp] = max(num, mp[temp])
        return res
