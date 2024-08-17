class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        res, visited = 0, set()
        surround = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def check(r, c):
            for x, y in surround:
                ro, co = r + x, c + y
                if (ro, co) in visited:
                    return False
            return True


        for i in range(m):
            for j in range(n):
                if board[i][j] == "X":
                    if check(i, j):
                        res += 1
                    visited.add((i, j))
        

        return res