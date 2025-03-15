class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
       
        def sw1():
            res = 0
            i = 0    
            while i < len(nums):
                j = i  
                while j < len(nums) and nums[i] == maxK and nums[i] == nums[j]:
                    res += (j-i+1)
                    j += 1
                if j != i:
                    i = j
                else: i += 1
            return res

        def sw2():
            pre, res, l = 0, 0, 0
            mp = defaultdict(int)
            for r in range(len(nums)):
                if nums[r] < minK or nums[r] > maxK:
                    pre = r+1
                    l = r+1
                    mp = defaultdict(int)
                if nums[r] == minK or nums[r] == maxK:
                    mp[nums[r]] += 1
                    while len(mp) == 2:
                        if nums[l] == minK or nums[l] == maxK:
                            mp[nums[l]] -= 1
                            if mp[nums[l]] == 0:
                                del mp[nums[l]]
                        l += 1
                if l > 0:
                    if (maxK in mp and nums[l-1] == minK) or (minK in mp and nums[l-1] == maxK):
                        res += (l-pre)
            return res
        if minK == maxK:
            return sw1()
        else:
            return sw2()
        