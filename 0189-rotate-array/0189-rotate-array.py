class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        remain = k % N
        if remain == 0: return
        temp = []
        for i in range(N-1, N-1-remain, -1):
            temp.append(nums[i])
        for i in range(N-1, remain-1, -1):
            nums[i] = nums[i-remain]
        for i in range(len(temp)):
            nums[i] = temp[len(temp)-i-1]
        