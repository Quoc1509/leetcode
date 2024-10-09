class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        surround = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        top = left = -1
        down = len(matrix)
        right = len(matrix[0])
        res = []
        r, c = 0, 0

        i = 0
        while len(res) < len(matrix)*len(matrix[0]):  
            res.append(matrix[r][c])     
            a, b = surround[i]
            
            if r+a == down or r+a == top or c+b == left or c+b == right:               
                if r+a == down:
                    right -= 1
                elif r+a == top:
                    left += 1
                elif c+b == left:
                    down -= 1
                elif c+b == right:
                    top += 1
                i += 1
                i %= 4
                a, b = surround[i]
            
            r = r+a
            c = c+b
            
        return res