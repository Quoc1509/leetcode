class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def BT(r, c, i):
            if i >= len(word):
                return True
            if r < 0 or r >= M or c < 0 or c >= N or board[r][c] != word[i]:
                return False
            w = board[r][c]
            board[r][c] = '.'
            for x, y in surround:
                ro, co = r+x, c+y
                
                if BT(ro, co, i+1):
                    return True

            board[r][c] = w

            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if BT(r, c, 0):
                    return True
        return False
            
            