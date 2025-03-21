class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = [(nums1[0]+nums2[0], 0, 0)]
        visit = set()
        while heap and len(res) < k:
            # print(heap)
            total, i1, i2 = heappop(heap)
            res.append((nums1[i1], nums2[i2]))
            if i1+1 < len(nums1) and (i1+1, i2) not in visit:
                heappush(heap, (nums1[i1+1]+nums2[i2], i1+1, i2))
                visit.add((i1+1, i2))
            if i2+1 < len(nums2) and (i1, i2+1) not in visit:
                heappush(heap, (nums1[i1]+nums2[i2+1], i1, i2+1))
                visit.add((i1, i2+1))
        return res