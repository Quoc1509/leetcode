class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        surround = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        M, N = len(rooms), len(rooms[0])
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    q.append((i, j))
        count = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for a, b in surround:
                    ro, co = r+a, c+b
                    if 0 <= ro < M and 0 <= co < N and rooms[ro][co] == 2147483647:
                        rooms[ro][co] = count
                        q.append((ro, co))
            count += 1

        