class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        temp = []
        for i in range(len(nums1)):
            temp.append([nums2[i], nums1[i]])
        temp.sort(reverse=True)
        heap = []
        total, res = 0, 0
        for i in temp:
            total += i[1]
            heapq.heappush(heap, i[1])
            if len(heap) > k:
                total -= heapq.heappop(heap)
                
            if len(heap) == k:
                res = max(res, total*i[0])
        return res