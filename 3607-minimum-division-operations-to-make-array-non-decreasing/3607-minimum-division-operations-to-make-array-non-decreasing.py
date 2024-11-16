class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                for j in range(2, int(sqrt(nums[i]))+1):
                    if nums[i] % j == 0:
                        nums[i] = j          
                        break
                if nums[i] > nums[i+1]:
                    return -1
                res += 1
        return res
            