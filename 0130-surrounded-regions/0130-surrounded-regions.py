class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        visit = set()
        for i in range(M):
            if board[i][0] == 'O':
                q.append((i, 0))
                visit.add((i, 0))
            if board[i][N-1] == 'O':
                q.append((i, N-1))
                visit.add((i, N-1))
        for i in range(N):
            if board[0][i] == 'O':
                q.append((0, i))
                visit.add((0, i))
            if board[M-1][i] == "O":
                q.append((M-1, i))
                visit.add((M-1, i))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in surround:
                    ro, co = r+x, c+y
                    if 0 <= ro < M and 0 <= co < N and (ro, co) not in visit and board[ro][co] == "O":
                        q.append((ro, co))
                        visit.add((ro, co))
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O' and (i, j) not in visit:
                    board[i][j] = 'X'

        