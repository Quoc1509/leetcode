class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = [False] * len(rooms)
        visit[0] = True
        key = deque(rooms[0])
        while key:
            a = key.popleft()
            if not visit[a]:
                visit[a] = True
                key.extend(rooms[a])
        for i in visit:
            if i == False: return False
        return True
    
