class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for i in nums:
            if not res or i > res[-1]:
                res.append(i)
            else:
                l, r = 0, len(res)-1
                while l <= r:
                    m = (l+r)//2
                    if res[m] < i:
                        l = m + 1
                    else:
                        r = m-1
                res[l] = i
        return len(res)