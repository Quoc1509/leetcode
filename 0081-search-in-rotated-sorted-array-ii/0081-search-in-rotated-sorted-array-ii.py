class Solution:

    def search(self, nums: List[int], target: int) -> bool:

        l, r = 0, len(nums)-1
        def helper(l, r):
            while l <= r:
                m = (l+r) // 2
                if nums[m] == target: return True
                if nums[m] < nums[r]:
                    if nums[m] < target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1
                elif nums[m] > nums[l]:
                    if nums[l] <= target < nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    return helper(l, m-1) or helper(m+1, r) 
            
            return False
        return helper(l, r)