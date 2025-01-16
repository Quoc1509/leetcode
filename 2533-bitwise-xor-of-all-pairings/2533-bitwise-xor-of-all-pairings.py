class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        if N%2 == 0 and M%2==0:
            return 0
        res1, res2 = 0, 0
        for num in nums1:
            res1 ^= num
        for num in nums2:
            res2 ^= num
        # print(res1, res2, res1^res2)
        if M%2==0:
            return res1
        elif N%2==0:
            return res2
        else:
            return res1^res2
