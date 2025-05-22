class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        heap = []
        q = 0
        diff = [0] * (len(nums)+1)
        for i in range(len(nums)):
            while q < len(queries) and queries[q][0] == i:
                heappush(heap, -queries[q][1])
                q += 1
            while nums[i] > diff[i]:
                if not heap or -heap[0] < i:
                    return -1
                end = -heappop(heap)
                diff[i] += 1
                diff[end+1] -= 1
            diff[i+1] += diff[i]
        return len(heap)
            
