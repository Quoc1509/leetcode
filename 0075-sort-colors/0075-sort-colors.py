class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for i in nums:
            if i == 0: red += 1
            if i == 1: white += 1
            if i == 2: blue += 1
        i = 0
        while i < len(nums):
            if red > 0:
                nums[i] = 0
                red -= 1
            elif white > 0:
                nums[i] = 1
                white -= 1
            else:
                nums[i] = 2

            i += 1

        