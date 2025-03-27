class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        res = []
        N = len(nums)
        i = 0
        while i < N:
            a = nums[i]
            j = i+1
            while j < N:
                b = nums[j]
                l, r = j+1, N-1
                while l < r:
                    if a + b + nums[l] + nums[r] == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        k = l + 1
                        while k < r and nums[l] == nums[k]:
                            k += 1
                        l = k
                    elif a + b + nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1

                k = j+1
                while k < N and nums[k] == nums[j]:
                    k += 1
                j = k 
            k = i+1
            while k < N and nums[k] == nums[i]:
                k += 1
            i = k
        return res
