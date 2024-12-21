class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)] 
        count = 0
        r, c = 0, 0
        while count < 9:
            square = set()
            i, j = r, c
            while i < r+3:
                while j < c+3:
                    num = board[i][j]
                    if num in square or num in row[i] or num in col[j]:
                        return False
                    if num != '.':
                        square.add(num)
                        row[i].add(num)
                        col[j].add(num)
                    j += 1
                i += 1
                j = c
            c += 3
            if c == 9:
                r += 3
                c = 0
            count += 1
        return True
                

