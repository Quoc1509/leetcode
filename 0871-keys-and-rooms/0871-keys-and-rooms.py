class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        visit.add(0)
        key = deque(rooms[0])
        while key:
            a = key.popleft()
            if a not in visit:
                visit.add(a)
                key.extend(rooms[a])
        
        return len(visit) == len(rooms)
    
