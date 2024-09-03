class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        temp = defaultdict(int)
        res = []
        heap = []
        for i in range(len(nums)):
            temp[nums[i]] += freq[i]
            # before temp = {3: 4, 2:3}
            heappush(heap, (-temp[nums[i]], nums[i]))

            while (-temp[heap[0][1]]) != heap[0][0]: 
                # update max value of frequence
                # example: after temp = {3: 2, 2:3} but in heap = [(4,3),(3, 2)]
                # pop the head to update the max 
                heappop(heap)

            res.append(-heap[0][0])
        return res

