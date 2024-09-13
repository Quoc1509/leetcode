class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(arr)+1)
        for i in range(len(arr)):
            prefix[i+1] = arr[i] ^ prefix[i]
        res = []
        for a, b in queries:
            res.append(prefix[a]^prefix[b+1])
        return res