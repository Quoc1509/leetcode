class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin = image[sr][sc]

        visit = set()
        def dfs(row, col):
            if (row < 0 or row >= len(image)) or (col < 0 or col >= len(image[row])):
                return
            if image[row][col] != origin or (row, col) in visit:
                # print(image[row][col])
                return
            visit.add((row, col))
            image[row][col] = color
            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)
        dfs(sr, sc)
        return image