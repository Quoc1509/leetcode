class Solution:
    def findScore(self, nums: List[int]) -> int:
        heap = []
        for i in range(len(nums)):
            heappush(heap, (nums[i], i))
        chosen = set()
        res = 0
        while heap:
            num, i = heappop(heap)
            if i not in chosen:
                res += num
                chosen.add(i)
                chosen.add(i+1)
                chosen.add(i-1)
        # print(res, chosen)
        return res