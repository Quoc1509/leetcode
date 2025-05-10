class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero1 = nums1.count(0)
        zero2 = nums2.count(0)

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        if zero1 > zero2:
            sum1, sum2 = sum2, sum1
            zero1, zero2 = zero2, zero1
        if zero1 == 0 and zero2 == 0 and sum1 != sum2:
            return -1
        if zero1 == 0 and sum1 < sum2:
            return -1
        if zero1 == 0 and sum1 < sum2+zero2:
            return -1

        return max(sum1+zero1, sum2+zero2)

