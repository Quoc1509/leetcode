class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        mp = defaultdict(list)
        for i in range(len(nums1)):
            mp[nums1[i]].append((nums2[i], i))
        res = [0] * len(nums1)
        temp = sorted(list(set(nums1)))
        total = 0
        heap = []
        for num in temp:
            if len(heap) > k:
                total -= heappop(heap) 
            temp = total
            for n, i in mp[num]:
                res[i] = total
                if len(heap) > k:
                    temp -= heappop(heap) 
                temp += n
                heappush(heap, n)
            total = temp
        return res