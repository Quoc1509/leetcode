class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        res = []
        for key, value in count1.items():
            if key in count2:
               res.extend([key] * min(count1[key], count2[key]))
        return res 