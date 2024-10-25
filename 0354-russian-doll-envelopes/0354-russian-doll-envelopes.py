class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: [x[0], -x[1]])
        A = []
        for a, b in envelopes:
            ind = bisect_left(A, b)
            if ind == len(A):
                A.append(b)
            else:
                A[ind] = b
        return len(A)