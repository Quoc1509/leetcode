class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        arr = [bin(nums[i]).count('1') for i in range(len(nums))]
        i = 0
        maxVal = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and arr[j] == arr[i]:
                j += 1
            minNum = min(nums[i:j])
            maxNum = max(nums[i:j])
            if minNum < maxVal:
                return False
            maxVal = maxNum
            i = j

                              
        return True