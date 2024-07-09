class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def bfs(index, visited):
            count = 1
            q = deque()
            q.append(bombs[i])
            visited.add(index)
            while q:
                for _ in range(len(q)):
                    curX, curY, curR = q.popleft()
                    for j in range(len(bombs)):
                        x, y, r = bombs[j]
                        dis = sqrt(pow((curX-x), 2) + pow((curY-y),2))
                        if j not in visited and dis <= curR:
                            q.append(bombs[j])
                            visited.add(j)
                            count += 1
            return count

        res = 1
        for i in range(len(bombs)):
            temp = bfs(i, set())
            res = max(temp, res)
            if res == len(bombs):
                return res
        return res


    