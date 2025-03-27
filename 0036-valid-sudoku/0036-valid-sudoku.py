from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        small = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row[i] or board[i][j] in col[j]:
                        return False
                                    
                    box_index = (i // 3, j // 3)
                    if board[i][j] in small[box_index]:
                        return False

                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    small[box_index].add(board[i][j])

        return True
