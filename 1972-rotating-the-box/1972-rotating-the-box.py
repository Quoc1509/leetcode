class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        M, N = len(box), len(box[0])
        res = [['.'] * M for _ in range(N)]
        for i in range(M):
            down = N-1
            for j in range(N-1, -1, -1):          
                if box[i][j] == '*':   
                    res[j][M-i-1] = '*'   
                    down = j-1       
                elif box[i][j] == '#':
                    res[down][M-i-1] = '#'
                    down -= 1
        return res