class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        M, N = len(board), len(board[0])
        move = defaultdict(int)
        
        count = 1
        direct = 1
        for i in range(M-1, -1, -1):
            a = 0 if direct > 0 else N-1
            b = -1 if direct < 0 else N
            for j in range(a, b, direct):
                if board[i][j] != -1:
                    move[count] = board[i][j]
                count += 1

            direct *= -1
        
        res = 0
        q = deque()
        q.append(1)
        visit = set()
        visit.add(1)
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur ==  M*N:
                    return res                   
                for i in range(1, 7):
                    new_cur = cur + i  
                    if new_cur in move:
                        new_cur = move[new_cur]
                    if new_cur not in visit:
                        q.append(new_cur)
                        visit.add(new_cur)
            res += 1
        return -1 

                
