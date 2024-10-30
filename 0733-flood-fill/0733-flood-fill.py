class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visit = set()
        pix = image[sr][sc]
        q = deque()
        q.append((sr, sc))
        visit.add((sr, sc))
        surround = [(1,0), (0, 1), (-1, 0), (0, -1)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                image[r][c] = color
                for x, y in surround:
                    ro, co = r+x, c+y
                    if 0 <= ro < len(image) and 0 <= co < len(image[0]) and (ro, co) not in visit and image[ro][co] == pix:
                        q.append((ro, co))
                        visit.add((ro, co))
        return image