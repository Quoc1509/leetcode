class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        res = [0] * len(queries)
        temp = []
        A = sorted([[e, i] for i, e in enumerate(queries)])
        heapify(items)
        cur = 0
        for i in range(len(queries)):
            
            while items and items[0][0] <= A[i][0]:
                temp = heappop(items)
                cur = max(cur, temp[1])
            res[A[i][1]] = cur
        return res
