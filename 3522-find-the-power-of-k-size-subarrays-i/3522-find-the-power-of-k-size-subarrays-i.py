class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        res = []
        l = 0
        for r in range(1, len(nums)):
            l = max(l, r-k+1)
            if nums[r] != nums[r-1]+1:
                l = r
            if r+1 >= k:
                res.append(nums[r] if r-l+1 == k else -1)
 
        return res




            
