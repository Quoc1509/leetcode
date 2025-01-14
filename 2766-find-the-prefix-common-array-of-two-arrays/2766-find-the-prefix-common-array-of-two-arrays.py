class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        mp = set()
        res = [0] * (len(A))
        for i in range(len(A)):
            if A[i] == B[i]:
                res[i] += 1
            else:
                if A[i] in mp:
                    res[i] += 1
                if B[i] in mp:
                    res[i] += 1
            res[i] += res[i-1] if i > 0 else 0
            mp.add(A[i])
            mp.add(B[i])
        return res