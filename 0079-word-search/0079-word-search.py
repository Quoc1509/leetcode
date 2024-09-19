class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])

        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c, ind):
            
            if ind == len(word): return True
            if r < 0 or r >= M or c < 0 or c >= N or board[r][c] != word[ind]: return False
            temp = board[r][c]
            board[r][c] = '#'
            for a, b in surround:
                row, col = r+a, c+b      

                if dfs(row, col, ind+1):
                    return True
            board[r][c] = temp
            return False


        for i in range(M):
            for j in range(N):
                if dfs(i, j, 0):
                    
                    return True

        return False
