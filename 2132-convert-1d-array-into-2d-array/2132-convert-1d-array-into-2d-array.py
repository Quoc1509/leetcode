class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n: return []
        res, row = [], []
        for i in original:
            row.append(i)

            if len(row) == n:
                res.append(row)
                row = []
        return res